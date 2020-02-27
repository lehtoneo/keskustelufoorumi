# Keskustelufoorumi

## Heroku

[Heroku](https://tsoha-tyoni.herokuapp.com/)

### Testitunnukset

Mikäli ei halua tehdä itse sovellukseen omia tunnuksia, voit käyttää seuraavia testitunnuksia:

*Normaali käyttäjä:*

Username: user  

Password: user

*Admin:*

Username: admin

Password: admin

## Dokumentaatio

[Käyttäjätarinat](https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/kayttajatarinat.md)

[Yhteenvetokyselyitä](https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/yhteenvetokyselyt.md)

[Asennusohje](https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/asennusohje.md)

[Käyttöohje](https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/kaytto-ohje.md)

[Create Table-lauseet](https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/createtablelauseet.md)

## Kuvaus

Sovellus on keskustelufoorumi, johon tulee kirjautua nähdäkseen keskustelut. Käyttäjä voi aloittaa keskustelun, poistaa aloittamansa keskutelun ja vastata omiin tai muiden aloittamiin keskusteluihin. Keskusteluja voi etsiä erilaisin kriteerein, kuten kategorioittain tai aloitusajan perusteella. Sovelluksessa on kaksi eri roolia: "user" ja "admin", joilla on hieman erilaiset toiminnot.

### Toteutetut toiminnallisuudet

- Kirjautuminen
- Käyttäjän luominen
- Keskustelun aloittaminen
- Keskusteluun vastaaminen
- Keskusteluiden listaaminen
- Keskusteluiden listaaminen kategorioittain
- Keskusteluiden listaaminen uusimmasta vanhimpaan ja vanhimmasta uusimpaan
- Kommenttien katselu
- Oman kommentin muokkaaminen
- Oman vastauksen ja keskustelun aloituksen poistaminen
- Oman keskustelun aiheen muokkaaminen
- Oman keskustelun kuvauksen muokkaaminen
- Kategorioiden lisäys itse aloittamalle keskustelulle
- Omien keskustelun aloituksien näyttäminen omalla sivulla
- Aktiivisimpien keskustelijoiden listaus
- Suosituimpien kategorioiden listaus

## TOTEUTUNUT Tietokantakaavio

<img src="https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/pics/tsohadbviim.png">
          
## TULEVAISUUDEN Tietokantakaavio

Ajatus tietokannasta, jos halutaan tulevaisuudessa lisätä tieto siitä, ketkä ovat lukeneet keskustelut. (Tässäkin tietokannassa roolit olisi omassa taulussa)

<img src="https://github.com/lehtoneo/keskustelufoorumi/blob/master/documentation/pics/dbPic.png">
