# Käyttäjätarinat

## Normaali käyttäjä: 

#### Pystyy aloittamaan uuden keskustelun

SQL-kysely:

```INSERT INTO Thread (id, title, description, posted, modified, user_id) VALUES (?, 'title_tähän', 'kuvaus_tähän', ?, ?, kirjautuneen_käyttäjän_id)```

Kysymysmerkkien kohdalle SQLAlchemy laittaa sopivat arvot: id:n kohdalle uniikin id:n, posted ja modified kenttien kohdalle SQLAlchemy laittaa ajan, jolloin kysely tehdään.



#### Pystyy kommentoimaan keskusteluihin

SQL-kysely:

```INSERT INTO Comment (id, text, posted, modified, thread_id, user_id) VALUES (?, 'kommentin_teksti', ?, ?, sen_keskustelun_id_johon_kommentoidaan, kirjautuneen_käyttäjän_id)``` 

Kysymysmerkkien kohdalle SQLAlchemy laittaa sopivat arvot: id:n kohdalle uniikin id:n, posted ja modified kenttien kohdalle SQLAlchemy laittaa ajan, jolloin kysely tehdään



#### Pystyy muokkaamaan omaa keskustelun aloitusta

SQL-kysely: 

```Update Thread SET Title ='uusi_title', modified = 'tämän_hetkinen_aika' WHERE id = muokattavan_keskustelun_id```

#### Pystyy muokkaamaan omaa 

#### Pystyy poistamaan oman keskustelun aloituksen

SQL-kysely:

```DELETE FROM Thread WHERE id = poistettavan_keskustelun_id```


#### Pystyy poistamaan oman kommentin

SQL-kysely: 

```DELETE FROM Comment WHERE id = poistettavan_kommentin_id```

#### Pystyy näkemään, ketkä ovat lukeneet keskusteluita


#### Pystyy etsimään keskusteluita kategorioittain


#### Pystyy näkemään ketkä ovat sovelluksen aktiivisimpia käyttäjiä

SQL-kysely:

```SELECT username, COUNT("user".id) AS count FROM "user" INNER JOIN Thread ON ("user".id = thread.user_id)' GROUP BY "user".id' ORDER BY count DESC```

#### Pystyy löytämään helposti omat keskustelun avauksensa
#### Pystyy lukemaan keskusteluita

## Admin
#### Pystyy tekemään kaiken mitä normaali käyttäjä pystyy tekemään
#### Pystyy poistamaan minkä tahansa keskustelun aloituksen
#### Pystyy poistamaan minkä tahansa kommentin

