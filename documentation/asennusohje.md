# Asennusohjeet

### Tarvittavat ohjelmat

Ohjeet olettavat, että konella, johon asennat ohjelman ainakin seuraavat ohjelmat: 


- [python](https://www.python.org/download) (sekä pythonin kirjasto venv)
- [pip](https://packaging.python.org/key_projects/#pip)


## Asennus paikallisesti

### Step 1. Lataaminen

##### Lataus vaihtoehto 1.

Mene projektin [juureen](https://github.com/lehtoneo/keskustelufoorumi), paina vihreää nappia clone or download. Jonka jälkeen pitäisi avautua valikko, jossa on mahdollisuus painaa nappia download zip.


Paina download zip. Latauksen jälkeen pura tiedosto haluaamaasi paikkaan.

##### Lataus vaihtoehto 2.

Tarvitset koneellesi [gitin](https://git-scm.com/downloads/) seurataksesi tätä vaihtoehtoa.

Luo kansio johon haluat tuoda projektin ja navigoi kyseiseen kansioon. Suorita komento 

```git clone https://github.com/lehtoneo/keskustelufoorumi.git```

### Step 2. Virtuaaliympäristön luominen ja käynnistäminen

Mene juuri lataamasi tiedoston juureen ja suorita komento:

```python -m venv venv```

Käynnistä virtuaaliympäristö seuraamalla ohjeita [täältä](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/), kohdasta activating virtual environment. 


### Step 3. Tarvittavien riippuvuuksien lataaminen

Suorita juurihakemistossa komento 
```pip install -r requirements.txt```

### Step 4. Käynnistys

Suorita juurihakemistossa komento


```python3 run.py```

tai

```python run.py```

Mikäli koneellasi on pythonin versioista ainoastaan python3. 

Nyt ohjelma pyörii lokaalisti osoitteessa http://localhost:5000/ 

## Projektin vieminen pilveen 

Seurataksesi ohjeita tarvitset:
- Herokun. Lataamiseen voit seurata ohjeita [täältä](https://devcenter.heroku.com/articles/heroku-cli). 
- Herokun työvälineet komento riville: https://devcenter.heroku.com/articles/heroku-cli
- Käyttäjän herokuun
- [PostgreSQL](https://www.postgresql.org/)-tietokannanhallintajärjestelmän. 
- [gitin](https://git-scm.com/downloads/)

### Step 1

Luodaan projektille paikka herokuun:

```heroku create oman_projektin_nimi``` 

### Step 2

Lisätään paikalliseen versionhallintaan herokusta

```git remote add heroku https://git.heroku.com/oman_projektin_nimi.git```

### Step 3 

Lähetetään projekti herokuun:

```git add .```

```git commit -m"init"```

```git push heroku master```

Projekti löytyy nyt osoitteesta  https://oman_projektin_nimi.herokuapp.com/

### Step 4

Luodaan projektille tietokanta:

```heroku addons:add heroku-postgresql:hobby-dev```

