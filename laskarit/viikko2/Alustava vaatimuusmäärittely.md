# Alustava vaatimuusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on olla pygamella totetutettu luolastoseikkailupeli, jossa pelaaja taistelee vihollisia vastaan ja ratkaisee pulmia luolaston eri osissa.

## Käyttöliittymäluonnos

![image](https://user-images.githubusercontent.com/80833101/113048217-f96bee00-91aa-11eb-8bca-47ef26081497.png)


Pelissä olisi tarkoituksena olla päävalikko, josta voit aloittaa pelin, tarkastella pelin asetuksia kuten näppäinkomentoja, katsoa kuka pelaaja on läpäissyt pelin korkeimmilla 
pisteillä, sekä poistua pelistä. Jos pelaaja aloittaa pelin, hänen tulee syöttää nimi. Tämän jälkeen pelaaja aloittaa pelin. 
Itse pelinäkymän olisi tarkoitus mukailla 16-bittisten pelien estetiikkaa, kuten esimerkiksi Pokemonissa tai Legend of Zeldassa.

## Perusversion tarjoama toiminnallisuus

* Pelaaja voi valita itselleen nimen, joka tulee näkymään päävalikon High Score - taulussa, jos hän läpäisee pelin nopeammin kuin muut. 
* Pelaaja pystyy liikkumaan, ampumaan tulipalloja jotka vahingoittavat vihollisia, hän menettää elämäpisteitä jos vihollinen osuu häneen, sekä hän voi saada elämäpisteitään 
takaisin esimerkiksi esineistä.
* Pelaaja voi poistua huoneesta, jolloin pelinäkymä vaihtuu toiseen huoneeseen. 

## Jatkokehitysideoita

* Päävalikosta voi valita millä hahmoluokalla käyttäjä haluaa pelata. 
    * esimerkiksi velho, taistelija, munkki  yms.
* Viholliset antavat kokemuspisteitä, ja kun tarpeeksi monta kokemuspistettä on kerätty, pelaaja saa uuden tason. Uudella tasolla pelaajan elämäpisteet kasvavat ja hänen 
hyökkäyksensä tekevät enemmän vahinkoa.
* Reppu, johon voi kerätä kertakäyttöesineitä. 
    * Kertakäyttöesineen käytöstä saa jotakin etua, kuten elämäpisteiden parannusta tai vahingon kasvaminen tietyksi ajaksi, mutta esine katoaa käytön jälkeen.
* Pelaaja voi löytää useita erilaisia sivuaseita.
    * Vain yksi sivuase voi olla kerrallaan käytössä, ja pelaaja voi vaihtaa niiden välillä tarpeen vaatiessa.
* Loppubossi
