# Opintojen seurantasovellus

Sovellus on tarkoitettu auttamaan opiskelijoita seuraamaan opintojen etenemistä ja kurssisuorituksia. Opiskelija voi lisätä sovellukseen hänen käymiään kursseja ja niistä saatuja tuloksia.

## Dokumentaatio

- [Changelog](https://github.com/isa-srs/ot-harjoitustyo2022/blob/main/dokumentaatio/changelog.md)
- [Työaikakirjanpito](https://github.com/isa-srs/ot-harjoitustyo2022/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/isa-srs/ot-harjoitustyo2022/blob/main/dokumentaatio/vaatimusmaarittely.md)

## Asennus

1. Asenna sovelluksen riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivikomennot

### Ohjelman suorittaminen

```bash
poetry run invoke start
```

### Testaus

```bash
poetry run invoke test
```

### Testikattavuus

```bash
poetry run invoke coverage-report
```

