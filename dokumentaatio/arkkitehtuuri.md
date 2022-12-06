# Arkkitehtuurikuvaus

## Sovelluksen rakenne

![Pakkauskaavio](./kuvat/pakkauskaavio.png)

## Sovelluslogiikka

```mermaid
 classDiagram
      Course "*" --> "1" User
      class User{
          username
          password
      }
      class Course{
          name
          credits
          user
      }
```

## Päätoiminnallisuudet

### Uuden käyttäjän luominen

![create_user_diagram](./kuvat/create_user_diagram.png)

