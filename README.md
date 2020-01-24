# Keskustelufoorumi

## Heroku

[Heroku](https://tsoha-tyoni.herokuapp.com/)

## Kuvaus

Sovellus on keskustelufoorumi, johon tulee kirjautua nähdäkseen keskustelut. Käyttäjä voi aloittaa keskustelun, poistaa aloittamansa keskutelun ja vastata omiin tai muiden aloittamiin keskusteluihin. Kirjoituksia voi etsiä erilaisin kriteerein, kuten kategorioittain tai aloitusajan perusteella. Sovellus pitää myös tietoa siitä, ketkä käyttäjistä ovat lukeneet keskustelun. Jos keskusteluun tulee uusi viesti, keskustelu näkyy käyttäjillä lukemattomana. Sovelluksessa on kaksi eri roolia: "user" ja "admin", joilla on hieman erilaiset toiminnot, joista lisää alla.

Joitakin toimintoja userilla:
- Kirjautuminen
- Keskustelun aloittaminen
- Keskusteluun vastaaminen
- Oman vastauksen tai keskustelun aloituksen muokkaaminen
- Oman vastauksen tai keskustelun aloituksen poistaminen

Toimintoja adminille:
- Kaikki userin toiminnot
- Kenen tahansa keskustelun aloituksen poistaminen
- Kenen tahansa vastauksen poistaminen

## Tietokantakaavio

<img src="https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/pics/tsohaDB.png">
