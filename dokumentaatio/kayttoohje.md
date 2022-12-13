# Käyttöohje

Lataa sovelluksen lähdekoodi viimeisimmästä releasesta.

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

Sovellus avautuu suoraan kirjautumisnäkymään. Uuden käyttäjän pääsee luomaan painamalla "Luo uusi tunnus" -nappia. 

## Sisäänkirjautuminen

Kirjautumisnäkymässä rekisteröitynyt käyttäjä pääsee kirjautumaan sisään. Tunnusten syöttämisen ja "Kirjaudu sisään" -napin painamisen jälkeen käyttäjä pääsee sovelluksen etusivulle.

## Kurssien lisääminen

Käyttäjä pääsee lisäämään kursseja sisäänkirjautumisen jälkeen. Etusivulla on "Lisää kurssi" -nappi, jota painamalla käyttäjä pääsee sivulle, johon voi syöttää kurssin tiedot. Kurssin tiedot tallentuvat tietokantaan ja tulevat kurssin lisäämisen jälkeen näkyville etusivulle.


