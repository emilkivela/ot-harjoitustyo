# Dungeon Crawl- peli 
Legend of Zelda-inspiroitunut 2D-dungeon crawler-peli joka on tehty pygamella.
Pelaaja taistelee luolastossa velholla vihollisia vastaan ja mahdollisesti
ratkoo pulmia.

## Toiminnallisuudet:

### Aloitusnäyttö
- Pelaaja voi syöttää nimen
- Ohjeet

### Pelinäkymä
- Pelaaja pystyy liikkumaan, ampumaan tulipalloja, tappamaan vihollisia ja vahingoittumaan
- Juokseva kello
- Pelaajan elämät
- Voi siirtyä tasosta toiseen
- Viholliset liikkuvat satunnaisiin suuntiin jos eivät ole ärsytettyjä
- Viholliset siirtyvät ärsytettyyn tilaan jos ovat 150:n pikselin päässä pelaajasta
- Viholliset liikkuvat kohti pelaajaa ärsytetyssä tilassa

### Game Over
- Jos pelaaja kuolee hänelle näytetään pelaajanimi ja paikalliset 10 nopeinta pelinläpäisyä ja niiden käyttäjänimet

### Game Completed
- Jos peli läpäistään, pelaajanimi ja läpäisyaika tallennetaan tietokantaan
- Nimi ja ja TOP10-läppäisyaikaa näytetään
