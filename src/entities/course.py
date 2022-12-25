class Course:
    """Luokka, joka kuvaa yksittäistä kurssia.
    """
    def __init__(self, name, credit, grade, user):
        """Luokan konstruktori, joka luo uuden kurssin.

        Args:
            name (str): Kurssin nimi
            grade (str): Kurssista saatu arvosana (0, jos kurssi edelleen kesken)
            credit (str): Kurssin opintopisteet
            user (str): Käyttäjän käyttäjänimi, joka lisäsi kurssin
        """

        self.name = name
        self.credit = credit
        self.grade = grade
        self.user = user
        