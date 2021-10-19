# Vytvoř jednoduchý skript v Pythonu, ve kterém budou deklarovány proměnné a s hodnotou 10 a b s hodnotou 7.
# Hodnoty proměnných vypiš na std výstup ve tvaru a je 10 a b je 7.
# Proveď prohození obsahu obou proměnných a znovu je vypiš na std výstup.
# Na std výstupu zobraz informaci, jakého datového typu jsou obě proměnné.
# Deklaruj tři proměnné s hodnotami "{} {}.", "Ahoj" a "Karle". Při pojmenování proměnných použij notaci camel-case.
# Zobraz na std výstupu formátovaný řetězec první proměnné přiřazením zbývajících proměnných tak, aby výsledný text tvořil smysluplnou větu.
# Kód skriptu odevzdej (přípona py, ne txt!).

a,b = 10, 7
print("a je", a, "a b je", b)
a,b = b,a
print("a je", a, "a b je", b)
print("a je", type(a), "a b je", type(b))

printTemplate = "{} {}."
userGreeting = "Ahoj"
userName = "Karle"

print(printTemplate.format(userGreeting, userName))