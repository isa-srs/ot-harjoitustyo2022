class User:
    """Luokka, joka kuvaa yksittäistä käyttäjää.
    """

    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username (str): Käyttäjänimi
            password (str): Salasana
        """

        self.username = username
        self.password = password
