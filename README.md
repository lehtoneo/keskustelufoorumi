# Keskustelufoorumi

## Heroku

[Heroku](https://tsoha-tyoni.herokuapp.com/)

### Testitunnukset

Mikäli ei halua tehdä itse sovellukseen omia tunnuksia, voit käyttää seuraavia testitunnuksia:

Username: username  
Password: password

## Dokumentaatio

[Käyttäjätarinat](https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/kayttajatarinat.md)

[Yhteenvetokyselyitä](https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/yhteenvetokyselyt.md)

[Asennusohje](https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/asennusohje.md)

[Käyttöohje](https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/kaytto-ohje.md)

## Kuvaus

Sovellus on keskustelufoorumi, johon tulee kirjautua nähdäkseen keskustelut. Käyttäjä voi aloittaa keskustelun, poistaa aloittamansa keskutelun ja vastata omiin tai muiden aloittamiin keskusteluihin. Kirjoituksia voi etsiä erilaisin kriteerein, kuten kategorioittain tai aloitusajan perusteella. Sovellus pitää myös tietoa siitä, ketkä käyttäjistä ovat lukeneet keskustelun. Jos keskusteluun tulee uusi viesti, keskustelu näkyy käyttäjillä lukemattomana. Sovelluksessa on kaksi eri roolia: "user" ja "admin", joilla on hieman erilaiset toiminnot.

### Toteutetut toiminnallisuudet

- Kirjautuminen
- Käyttäjän luominen
- Keskustelun aloittaminen
- Keskusteluun vastaaminen
- Keskusteluiden listaaminen
- Kommenttien katselu
- Oman vastauksen ja keskustelun aloituksen poistaminen
- Oman keskustelun aiheen muokkaaminen
- Oman keskustelun kuvauksen muokkaaminen
- Omien keskustelun aloituksien näyttäminen omalla sivulla
- Yhden kategorian lisäys keskustelun aloitukselle
- Aktiivisimpien keskustelijoiden listaus


## TOTEUTUNUT Tietokantakaavio

<img src="https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/pics/tsohadbtoteutunut.png">
          
## Tietokantakaavio

Ajatus tietokannasta, jos halutaan tulevaisuudessa lisätä tieto siitä, ketkä ovat lukeneet keskustelut.

<img src="https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/pics/dbPic.png">
