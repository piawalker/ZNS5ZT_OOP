class Berles:
    def __init__(self, auto, datum: str):
        self._auto = auto
        self._datum = datum

    def get_auto(self):
        return self._auto

    def get_datum(self):
        return self._datum

    def __str__(self):
        return f"Bérlés: {self._auto.get_rendszam()} - {self._auto.get_tipus()} | Dátum: {self._datum}"