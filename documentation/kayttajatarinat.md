# Käyttäjätarinat

## Normaali käyttäjä: 

#### Pystyy aloittamaan uuden keskustelun

SQL-kysely:

```INSERT INTO Thread (id, title, description, posted, modified, user_id) VALUES (?, 'title_tähän', 'kuvaus_tähän', ?, ?, kirjautuneen_käyttäjän_id)```

Kysymysmerkkien kohdalle SQLAlchemy laittaa sopivat arvot: id:n kohdalle uniikin id:n, posted ja modified kenttien kohdalle SQLAlchemy laittaa ajan, jolloin kysely tehdään.



#### Pystyy vastaamaan keskusteluihin

SQL-kysely:

```INSERT INTO Comment (id, text, posted, modified, thread_id, user_id) VALUES (?, 'kommentin_teksti', ?, ?, sen_keskustelun_id_johon_vastataan, kirjautuneen_käyttäjän_id)``` 

Kysymysmerkkien kohdalle SQLAlchemy laittaa sopivat arvot: id:n kohdalle uniikin id:n, posted ja modified kenttien kohdalle SQLAlchemy laittaa ajan, jolloin kysely tehdään



#### Pystyy muokkaamaan omaa keskustelun aloitusta

SQL-kysely: 

```Update Thread SET Title ='uusi_title', modified = 'tämän_hetkinen_aika' WHERE id = muokattavan_keskustelun_id```

#### Pystyy muokkaamaan omaa kommenttia

#### Pystyy poistamaan oman keskustelun aloituksen

SQL-kysely

```DELETE FROM Thread WHERE id = poistettavan_keskustelun_id```


#### Pystyy poistamaan oman vastauksen
#### Pystyy näkemään, ketkä ovat lukeneet keskusteluita
#### Pystyy etsimään keskusteluita kategorioittain
#### Pystyy näkemään ketkä ovat sovelluksen aktiivisimpia käyttäjiä
#### Pystyy löytämään helposti omat keskustelun avauksensa

## Admin
#### Pystyy tekemään kaiken mitä normaali käyttäjä pystyy tekemään
#### Pystyy poistamaan minkä tahansa keskustelun aloituksen
#### Pystyy poistamaan minkä tahansa kommentin

