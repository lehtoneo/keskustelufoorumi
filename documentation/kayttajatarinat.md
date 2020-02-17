# Käyttäjätarinat

## Normaali käyttäjä: 
- Pystyy aloittamaan uuden keskustelun
SQL Kysely:

```INSERT INTO Thread (id, title, description, posted, modified, user_id) VALUES (?, 'title tähän', 'kuvaus tähän', ?, ?, kirjautuneen käyttäjän id tähän)```

Kysymysmerkkien kohdalle SQL-alchemy laittaa sopivat arvot: id:n kohdalle uniikin id:n, posted ja modified kenttien kohdalle sql alchemy laittaa ajan, jolloin kysely tehdään.



- Pystyy vastaamaan keskusteluihin
- Pystyy muokkaamaan omaa keskustelun aloitusta
- Pystyy muokkaamaan omaa kommenttia
- Pystyy poistamaan oman keskustelun aloituksen
- Pystyy poistamaan oman vastauksen
- Pystyy näkemään, ketkä ovat lukeneet keskusteluita
- Pystyy etsimään keskusteluita kategorioittain
- Pystyy näkemään ketkä ovat sovelluksen aktiivisimpia käyttäjiä
- Pystyy löytämään helposti omat keskustelun avauksensa

## Admin
- Pystyy tekemään kaiken mitä normaali käyttäjä pystyy tekemään
- Pystyy poistamaan minkä tahansa keskustelun aloituksen
- Pystyy poistamaan minkä tahansa kommentin

