# Asennusohje

### Tarvittavat ohjelmat

Ohjeet olettavat, että konella, johon asennat ohjelman ainakin seuraavat ohjelmat: 


- [python](https://www.python.org/download) (sekä pythonin kirjastot pip ja venv)

## Asennus

### 1. Lataaminen ja purkaminen

Mene projektin [juureen](https://github.com/lehtoneo/keskustelufoorumi), paina vihreää nappia clone or download. Jonka jälkeen pitäisi avautua valikko, jossa on mahdollisuus painaa nappia download zip.


Paina download zip. Latauksen jälkeen pura tiedosto haluaamaasi paikkaan.

### 2. Virtuaaliympäristön luominen ja käynnistäminen

Mene juuri lataamasi tiedoston juureen ja suorita komento:

```python -m venv venv```

Käynnistä virtuaaliympäristö seuraamalla ohjeita [täältä](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/), kohdasta activating virtual environment. 


### 3. Tarvittavien riippuvuuksien lataaminen

Suorita juurihakemistossa komento 
```pip install -r requirements.txt```

### 4. Käynnistys

Suorita juurihakemistossa komento

```python3 run.py```

tai

```python run.py```

Mikäli koneellasi on pythonin versioista ainoastaan python3. 

Nyt ohjelma pyörii lokaalisti osoitteessa http://localhost:5000/ 


