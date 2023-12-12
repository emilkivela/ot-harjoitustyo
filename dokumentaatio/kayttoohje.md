# Käyttöohje

## Konfigurointi
Tietokannan nimen voi määrittää käynnistyshakemistossa *.env*-tiedostossa.
Tietokanta luodaan automaattisesti *src*-hakemistoon, jos sitä ei ole vielä olemassa.
Tiedoston muoto on seuraavanlainen:
```
DATABASE_FILENAME=database.db

## Ohjelman käynnistäminen
Asenna riippuvuudet komennolla:
```
poetry install
```

Alusta tietokanta komennolla:
```
poetry run invoke build
```

Käynnistä ohjelma komennolla:
```
poetry run invoke start
```

## Pelin pelaaminen
Peli avautuu päävalikkoon:
![Päävalikko](./kuvat/paavalikko.png)

Syötä pelaajatunnuksesi klikkaamalla laatikkoa, kirjoittamalla se ja painamalla ENTER:
![Pelaajatunnus](./kuvat/pelaajatunnus.png)

Liikuta velhoa nuolinäppäimillä ja ammu tulipalloja välilyönnillä:
![Peli](./kuvat/game.png)

Kun kuolet näet 10 nopeinta pelin läpäissyttä:
![GameOver](./kuvat/gameover.png)
