# Käyttäjätarinat ja niihin liittyvät SQL-kyselyt

Huom. Joissain kyselyissä on hipsut "" sen takia, että ne toimisivat myös pilvessä PostgreSQL:ssä.

# Toteutuneet

## Normaali käyttäjä: 

#### Pystyy aloittamaan uuden keskustelun

SQL-kysely, jolla lisätään keskustelu thread tauluun:

```SQL 
INSERT INTO Thread (id, title, description, posted, user_id) 
VALUES (?, 'title_tähän', 'kuvaus_tähän', ?, kirjautuneen_käyttäjän_id);
```

Kysymysmerkkien kohdalle SQLAlchemy laittaa sopivat arvot: id:n kohdalle uniikin id:n ja posted kentän kohdalle SQLAlchemy laittaa ajan, jolloin kysely tehdään.

SQL-kysely, jolla lisätään kategoria keskustelulle:

```SQL
INSERT INTO Thread_Category (id, thread_id, category_id)
VALUES (?, lisätyn_threadin_id, categorian_id);
```



#### Pystyy kommentoimaan keskusteluihin


```SQL
INSERT INTO Comment (id, text, posted, thread_id, user_id) 
VALUES (?, 'kommentin_teksti', ?, sen_keskustelun_id_johon_kommentoidaan, kirjautuneen_käyttäjän_id);
``` 

Kysymysmerkkien kohdalle SQLAlchemy laittaa sopivat arvot: id:n kohdalle uniikin id:n ja posted kentän kohdalle SQLAlchemy laittaa ajan, jolloin kysely tehdään



#### Pystyy muokkaamaan omaa keskustelun aloitusta

SQL-kysely, jolla muokataan aihetta

```SQL
Update Thread SET Title ='uusi_title', modified = 'tämän_hetkinen_aika' 
WHERE id = muokattavan_keskustelun_id;
```

SQL-kysely, jolla muokataan kuvausta

```SQL
Update Thread SET Description ='uusi_kuvaus', modified = 'tämän_hetkinen_aika' 
WHERE id = muokattavan_keskustelun_id;
```


#### Pystyy poistamaan oman keskustelun aloituksen


```SQL 
DELETE FROM Thread WHERE id = poistettavan_keskustelun_id;
```


#### Pystyy poistamaan oman kommentin


```SQL 
DELETE FROM Comment WHERE id = poistettavan_kommentin_id;
```

#### Pystyy muokkaamaan omaa kommenttia

```SQL
Update Comment SET comment_text ='uusi kommentti', modified = 'tämän_hetkinen_aika' 
WHERE id = muokattavan_kommentin_id;
```

#### Pystyy etsimään keskusteluita

##### Ajan perusteella
Uusimmasta vanhimpaan:

```SQL
SELECT * FROM thread 
ORDER BY thread.posted DESC;
```

Vanhimmasta uusimpaan:

```SQL
SELECT * FROM thread 
ORDER BY thread.posted ASC;
```
##### Kategorioittain

```SQL
SELECT *  
FROM thread
WHERE EXISTS (SELECT 1
FROM "Thread_Category"
WHERE thread.id = "Thread_Category".thread_id AND "Thread_Category".category_id = kategorian_id)
```

##### Sekä ajan, että kategorian perusteella

Kysely hakee keskustelut uusimmasta vanhimpaan. Jos halutaan vanhimmasta uusimpaan, vaihdetaan vain lopusta DESC -> ASC 

```SQL
SELECT * FROM thread
WHERE EXISTS (SELECT 1
FROM "Thread_Category"
WHERE thread.id = "Thread_Category".thread_id AND "Thread_Category".category_id = kategorian_id) ORDER BY thread.posted DESC;
```



#### Pystyy näkemään ketkä ovat sovelluksen aktiivisimpia käyttäjiä


```SQL 
SELECT username, COUNT(user.id) AS count FROM user 
INNER JOIN Thread ON (user.id = thread.user_id)
GROUP BY user.id 
ORDER BY count DESC;
```

#### Pystyy löytämään helposti omat keskustelun avauksensa


```SQL
SELECT * FROM Thread
WHERE user_id = kirjautuneen_käyttäjän_id;
```
#### Pystyy lukemaan keskusteluita

SQL-kysely, jolla saa kaikki tietyn threadin tiedot:

```SQL
SELECT * FROM Thread
WHERE id = threadin_id;
```

SQL-kysely, jolla saadaan auki tietyn threadin kommentit ja siihen liittyvät oleelliset tiedot: 

```SQL
SELECT username, comment_text, posted, user.id, comment.id FROM user
INNER JOIN Comment ON (user_id = user.id)
WHERE (thread_id = tahan_threadin_id);
```

#### Pystyy näkemään aktiivisimmat käyttäjät

```SQL
SELECT username, COUNT("user".id) AS count FROM "user"
INNER JOIN Thread ON ("user".id = thread.user_id)'
GROUP BY user.id
ORDER BY count DESC;
```

#### Pystyy näkemään suosituimmat kategoriat
```SQL
SELECT name, COUNT(category.id) AS count FROM category
INNER JOIN Thread__Category ON (category.id == Thread__Category.category_id)
GROUP BY category.id
ORDER BY count DESC;
``` 

## Admin

#### Pystyy tekemään kaiken mitä normaali käyttäjä pystyy tekemään
#### Pystyy poistamaan minkä tahansa keskustelun aloituksen
SQL lause on sama kuin normaalilla käyttäjällä, mutta adminin ollessa kirjautunut, ei tarkisteta onko keskustelu oma.
#### Pystyy poistamaan minkä tahansa kommentin
SQL lause on sama kuin normaalilla käyttäjällä, mutta adminin ollessa kirjautunut, ei tarkisteta onko kommentti oma.

# Toistaiseksi toteuttamattomat

## Käyttäjä

##### Pystyy näkemään, ketkä ovat lukeneet keskusteluita

