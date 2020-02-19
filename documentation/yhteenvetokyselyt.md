# Yhteenvetokyselyt

### 1. 

Kysely, joka laskee aktiivisimmat käyttäjät sen perusteella, kuinka monta keskustelua käyttäjä on aloittanut. Kyselyä käytetään, kun avataan sivu, jossa on aktiivisimmat käyttäjät. Metodi, joka käyttää kyselyä löytyy [täältä](https://github.com/lehtoneo/keskustelufoorumi/blob/master/application/auth/models.py)

```SQL
  SELECT username, COUNT(user.id) AS count FROM user
  INNER JOIN Thread ON ("user".id = thread.user_id)'
  GROUP BY user.id
  ORDER BY count DESC;

```

### 2.

Kysely, jolla saadaan suosituimmat kategoriat

```SQL
SELECT name, COUNT(category.id) AS count FROM category
INNER JOIN Thread__Category ON (category.id == Thread__Category.category_id)
GROUP BY category.id
ORDER BY count DESC;
```

