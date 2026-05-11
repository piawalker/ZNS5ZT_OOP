from auto import Auto


class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._teherbiras = teherbiras

    def get_teherbiras(self):
        return self._teherbiras

    def info(self):
        return f"Teherautó | {self._rendszam} | {self._tipus} | {self._berleti_dij} Ft/nap | {self._teherbiras} kg"