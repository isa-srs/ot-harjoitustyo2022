class Course:
    """Luokka, joka kuvaa yksittäistä kurssia.
    """
    def __init__(self, name, credit, grade, user):
        """Luokan konstruktori, joka luo uuden kurssin.

        Args:
            name (str): Kurssin nimi
            credits (str): Kurssin opintopisteet
            user (str): Käyttäjän käyttäjänimi, joka lisäsi kurssin
        """

        self.name = name
        self.credit = credit
        self.grade = grade
        self.user = user
        