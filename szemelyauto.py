from auto import Auto


class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, ulesek_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._ulesek_szama = ulesek_szama

    def get_ulesek_szama(self):
        return self._ulesek_szama

    def info(self):
        return f"Személyautó | {self._rendszam} | {self._tipus} | {self._berleti_dij} Ft/nap | {self._ulesek_szama} ülés"