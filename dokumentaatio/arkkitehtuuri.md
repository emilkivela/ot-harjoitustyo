# Arkkitehtuurikuvaus

## Rakenne
![Pakkauskaavio](./kuvat/package_diagram.png)
Kansion *game* sisällä oleva koodi huolehtii itse pelistä ja sen 
käyttöliittymästä, kansio *entities* sisältää luokkia joita peli käytättää, kuten
spritet, *services* sisältäää yleisiä tarpeellisia funktioita ja *repositories*
huolehtii tietokannasta.

## Käyttöliittymä
Pelissä on kolme erilaista näkymää:
- Aloitusnäyttö, jossa voi asettaa käyttäjänimen sekä jossa ohjeet kontrolleihin
- Itse peli
- Lopetusnäyttö, kun pelaaja kuolee, näyttää pelaaja nimen sekä scoreboardin

## Sovelluslogiikka
Seuraavassa luokkakaaviossa esitellään pelin luokkien riippuvuudet

```mermaid
 classDiagram
    GameLoop "1" -- "1" Level
    GameLoop "1" -- "1" Clock
    GameLoop "1" -- "1" EventQueue
    GameLoop "1" -- "1" Renderer
    Renderer "1" -- "1" TextBox
    Level "1" -- "1" Wizard
    class Wizard {
        health
    }
    Level "1" -- "2" Skeleton
    class Skeleton {
        health
    }
    Wizard "1" -- "3" Fireball
    Wizard "1" -- "1" HealthBar
    Level "1" -- "*" Cobble
    Level "1" -- "*" Brick
    Level "1" -- "*" Door
```
## Toiminnallisuudet

### Velhon liikuttaminen - sekvenssikaavio
```mermaid
sequenceDiagram
    participant User
    participant main
    participant GameLoop
    participant Level
    participant Wizard
    Participant Renderer
    User ->> main: input(Right arrow click)
    main ->> GameLoop: pygame.event(type = CLICKDOWN, key = K_RIGHT)
    GameLoop ->> Level: move_player(dx=2)
    Level ->> Wizard: wizard.move_ip(dx=2)
    Wizard ->> Renderer: wizard sprite position changes
    Renderer ->> GameLoop: render()
    GameLoop ->> main: 
    main ->> User: Wizard position changes
```
