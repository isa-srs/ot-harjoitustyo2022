# Käyttöohje

Lataa sovelluksen lähdekoodi [Releaset](https://github.com/isa-srs/ot-harjoitustyo2022/releases)-sivulta löytyvästä viimeisimmästä releasesta.

## Sovelluksen käyttöönotto

Sovelluksen lataamisen jälkeen asenna poetry komennolla:

```bash
poetry install
```

Alusta sovellus komennolla:

```bash
poetry run invoke build
```

Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Uuden käyttäjän luominen

Sovellus avautuu suoraan kirjautumisnäkymään. Uuden käyttäjän pääsee luomaan painamalla "Luo uusi tunnus" -nappia. Mikäli sekä käyttäjänimi että salasana ovat 4-10 merkin pituisia, eikä käyttäjänimeä ole varattu, uuden käyttäjän luonti onnistuu painamalla sivulla näkyvää "Luo käyttäjä"-painiketta. 

## Sisäänkirjautuminen

Kirjautumisnäkymässä rekisteröitynyt käyttäjä pääsee kirjautumaan sisään. Tunnusten syöttämisen ja "Kirjaudu sisään" -napin painamisen jälkeen käyttäjä pääsee sovelluksen kurssinäkymään eli etusivulle.

## Kurssien lisääminen

Käyttäjä pääsee lisäämään kursseja sisäänkirjautumisen jälkeen. Etusivulla on "Lisää kurssi" -nappi, jota painamalla käyttäjä pääsee sivulle, johon voi syöttää kurssin tiedot. Kurssin tiedot tallentuvat tietokantaan ja tulevat kurssin lisäämisen jälkeen näkyville etusivulle. 

## Kurssien tietojen päivittäminen

Kun kurssi halutaan merkitä suoritetuksi, onnistuu se painamalla kyseisen kurssin vieressä olevaa "Merkitse suoritetuksi"-painiketta. Tämä vie sivulle, jossa käyttäjä voi vielä antaa kurssista saadun arvosanan. Sopivan arvosanan (välillä 1-5) syöttämisen ja "Merkitse suoritetuksi"-painikkeen painamisen jälkeen kurssin tilanne päivittyy suoritetuksi ja käyttäjä viedään takaisin etusivunäkymään. Kurssin kohdalle pitäisi olla päivittynyt annettu arvosana. 

Jokaisen kurssin vieressä on lisäksi painike "Poista", jota painamalla kyseinen kurssi poistuu etusivulta ja tietokannasta. Kurssi ei kuitenkaan poistu suoraan näkymästä, vaan sivulta täytyy ensin poistua (esim. kirjautumalla ulos) ja sitten palata etusivulle. Jos kurssia ei ollut tarkoitus poistaa, voi sen aina lisätä uudestaan samalla tavalla kuin kursseja normaalistikin lisätään. 

Kurssien nimiä tai opintopistemääriä ei ole suoraan mahdollista muuttaa, mutta tämäkin onnistuu ensin poistamalla kurssin ja sitten lisäämällä sen uudestaan uusilla halutuilla tiedoilla.

