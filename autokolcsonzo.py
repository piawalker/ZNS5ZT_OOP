from berles import Berles


class Autokolcsonzo:
    def __init__(self, nev: str):
        self._nev = nev
        self._autok = []
        self._berlesek = []

    def add_auto(self, auto):
        self._autok.append(auto)

    def add_berles(self, berles):
        self._berlesek.append(berles)

    def listaz_autok(self):
        for auto in self._autok:
            print(auto.info())

    def listaz_berlesek(self):
        if len(self._berlesek) == 0:
            print("Nincs aktív bérlés.")
            return

        for i, berles in enumerate(self._berlesek, start=1):
            print(f"{i}. {berles}")

    def auto_elerheto(self, rendszam: str, datum: str):
        for berles in self._berlesek:
            if berles.get_auto().get_rendszam() == rendszam and berles.get_datum() == datum:
                return False
        return True

    def berel_auto(self, rendszam: str, datum: str):
        if datum.strip() == "":
            raise ValueError("A dátum nem lehet üres!")

        auto = None
        for a in self._autok:
            if a.get_rendszam() == rendszam:
                auto = a
                break

        if auto is None:
            raise ValueError("Nincs ilyen rendszámú autó!")

        if not self.auto_elerheto(rendszam, datum):
            raise ValueError("Ez az autó ezen a napon már ki van bérelve!")

        uj_berles = Berles(auto, datum)
        self._berlesek.append(uj_berles)

        return auto.get_berleti_dij()

    def lemond_berles(self, rendszam: str, datum: str):
        for berles in self._berlesek:
            if berles.get_auto().get_rendszam() == rendszam and berles.get_datum() == datum:
                self._berlesek.remove(berles)
                return True

        raise ValueError("Nem található ilyen bérlés, ezért nem mondható le!")