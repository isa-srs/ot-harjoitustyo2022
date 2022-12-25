# Changelog

## Viikko 3

- Alustava käyttöliittymärakenne ja lisätty eri näkymiä vastaavat luokat
- Lisätty AppService-luokka, jossa toteutuu sovelluksen toiminta
- Lisätty UserRepository-luokka, jossa tallennetaan uusi käyttäjä tietokantaan
- Lisätty testit, että uuden käyttäjän luominen toimii oikein
  - Huom! Pytestin ja coverage-riippuvuuksien asentamisessa ongelmia, joten ne eivät toimi. Testit kuitenkin olemassa tiedostossa src/tests/service_test.py

## Viikko 4

- Lisätty CourseRepository-luokka, joka vastaa kurssien lisäämisestä ja tallentamisesta tietokantaan
- Kirjautunut käyttäjä pystyy lisäämään uusia kursseja
- Lisätty testit, että UserRepository- ja CourseRepository-luokat tallentavat uudet käyttäjät/kurssit oikein ja ne ovat löydettävissä tietokannasta
  - Riippuvuusten asennuksessa aikaisemmin ilmennyt ongelma korjattu; testit ja testikattavuusraportin luominen toimivat

## Viikko 5

- Opiskelija näkee omat kurssinsa etusivulla

## Viikko 6

- Opiskelija näkee etusivulla kurssien opintopisteiden kokonaismäärän

## Viikko 7

- Loppupalautus
- Opiskelija näkee etusivulla kurssien opintopisteiden kokonaismäärän (korjattu)
- Opiskelija näkee vain omat kurssinsa etusivulla (ei kaikkia tietokannasta löytyviä kursseja)
- Opiskelija voi merkitä kursseja suoritetuiksi
- Lisätty näkymä SetGrade ja sitä vastaava SetGrade-luokka
- Lisätty testejä CourseRepositorylle

