# Import funkce sqrt z knihovny math
from math import sqrt

# Vytvoření funkce pro výpočet kvadratické rovnice, kde se zadají 3 parametry a, b, c
def solve(a, b, c):

    # Výpočet diskriminantu
    D = (b ** 2) - 4 * a * c
    if D < 0:
        # Pokud je diskriminant menší než nula výsledek nemá řešení
        print("No Solution!")
    else:
        D = sqrt((b ** 2) - 4 * a * c)


    # Výpočet kvadratické funkce, podle výsledku z diskriminantu
    if D > 0:
        # Pokud je diskriminant větší než nula výsledek má 2 řešení
        x1 = ((-1) * (b) + D) / (2 * a)
        x2 = ((-1) * (b) - D) / (2 * a)
        print("Solution: k{", x1, ";", x2, "}")

    if D == 0:
        # Pokud je diskriminant nula výsledek má 1 řešení
        x = (-1) * (b) / (2 * a)
        print("Solution: k{0;", x, "}")


if __name__ == '__main__':
    while True:
        try:
            # Input do proměnných a,b,c
            a = float(input("Enter A: "))
            b = float(input("Enter B: "))
            c = float(input("Enter C: "))

            # Volám funkci solve a vkládám do ní parametry a,b,c
            solve(a, b, c)
            exit()

        # Kdyby uživatel zadal něco jiného než číslo 
        except ValueError:
            print("No numbers were given.")

        # Když uživatel chce odejít pomocí CTRL+C tak se program ukončí bez chyby
        except KeyboardInterrupt:
            print("\n Safely Exitting.")
            exit()