from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from berles import Berles


def elore_betolt():
    kolcsonzo = Autokolcsonzo("SpeedRent")

    a1 = Szemelyauto("BMW-123", "BMW M4 Competition", 12000, 4)
    a2 = Szemelyauto("GT-911", "Porsche 911 GT3 RS", 11000, 2)
    a3 = Teherauto("AMG-063", "Mercedes-Benz Sprinter 63 AMG", 20000, 3500)

    kolcsonzo.add_auto(a1)
    kolcsonzo.add_auto(a2)
    kolcsonzo.add_auto(a3)

    kolcsonzo.add_berles(Berles(a1, "2026-05-10"))
    kolcsonzo.add_berles(Berles(a1, "2026-05-11"))
    kolcsonzo.add_berles(Berles(a2, "2026-05-12"))
    kolcsonzo.add_berles(Berles(a3, "2026-05-13"))

    return kolcsonzo


def menu():
    kolcsonzo = elore_betolt()

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ RENDSZER ---")
        print("1 - Autók listázása")
        print("2 - Autó bérlése")
        print("3 - Bérlés lemondása")
        print("4 - Bérlések listázása")
        print("0 - Kilépés")

        valasztas = input("Választás: ")

        try:
            if valasztas == "1":
                kolcsonzo.listaz_autok()

            elif valasztas == "2":
                rendszam = input("Add meg a rendszámot: ")
                datum = input("Add meg a dátumot (YYYY-MM-DD): ")
                ar = kolcsonzo.berel_auto(rendszam, datum)
                print(f"Sikeres bérlés! Ár: {ar} Ft")

            elif valasztas == "3":
                rendszam = input("Add meg a rendszámot: ")
                datum = input("Add meg a dátumot: ")
                kolcsonzo.lemond_berles(rendszam, datum)
                print("Bérlés sikeresen lemondva.")

            elif valasztas == "4":
                kolcsonzo.listaz_berlesek()

            elif valasztas == "0":
                print("Kilépés...")
                break

            else:
                print("Hibás választás!")

        except ValueError as e:
            print("HIBA:", e)


if __name__ == "__main__":
    menu()