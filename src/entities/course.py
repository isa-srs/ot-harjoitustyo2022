class Course:
    """Luokka, joka kuvaa yksittäistä kurssia.
    """
    def __init__(self, name, credits, user):
        """Luokan konstruktori, joka luo uuden kurssin.

        Args:
            name (str): Kurssin nimi
            credits (str): Kurssin opintopisteet
            user (str): Käyttäjän käyttäjänimi, joka lisäsi kurssin
        """

        self.name = name
        self.credits = credits
        self.user = user
        