# Yhteenvetokyselyt

### 1. 

Kysely, joka laskee aktiivisimmat käyttäjät sen perusteella, kuinka monta keskustelua käyttäjä on aloittanut. Kyselyä käytetään, kun avataan sivu, jossa on aktiivisimmat käyttäjät.

```
  SELECT username, COUNT(user.id) AS count FROM user
                       INNER JOIN Thread ON ("user".id = thread.user_id)'
                       GROUP BY user.id
                       ORDER BY count DESC;

```
