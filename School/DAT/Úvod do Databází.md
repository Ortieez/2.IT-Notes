# Úvod do databází
- Data jsou organizována v databázích (DB)
- Data jsou řízena balíkem programů, který se nazývá systém řízení bází dat (SŘBD)
- Databáze a systém řízení bází dat tvoří databázový systém (DBS)

## `DB + SŘBD = DBS`

# DB
- Jedná se o datovou základnu
- Data jsou organizována v komplikovanější centrálně zpracovávané struktuře dat, zvané databáze.
- Databáze zahrnuje čtyři komponenty:

	1. Datové prvky (pro zachycení elementárních hodnot jako například: Jméno, Příjmení, Adresa, …)
	2. Vztahy mezi prvky dat (jednotlivé vazby mezi prvky dat)
	3. Integritní omezení - IO (podmínky pro data v databázi)
	4. Schéma (popis dat, vztahů a IO srozumitelný pro uživatele)
	
- Data jsou obvykle uložená v patřičných formátech na vnějších paměťových médiích
- Široká veřejnost si pod tímto pojmem představuje kompletní databázový systém, tedy data i software, který s daty manipuluje

# Databázové Modely
Z hlediska ukládání dat a vazeb mezi nimi dělíme databáze na:
- [[Hierarchická DB]]
- [[Síťová DB]]
- [[Relační DB]]
- Objektová DB
- Objektově relační DB

# Požadavky na SŘBD

- Perzistence (přetrvávání dat v databázi nezávisle na programech či aktivitách uživatele)
- Sdílení dat (víceuživatelský přístup)
- Spolehlivost
- Ochrana dat (fyzická, autorizace)
- Neredundance (zbytečně se neopakující prvky v databázi)
- Nezávislost (nezávislý přístup k datům uložených v různých platformách)

# Služby SŘBD
- Transakční zpracování
- Řízení souběžného přístupu více uživatelů
- Řízení zotavení z chyb
- Řízení utajení dat
- Zahrnutí jazykových prostředků
- Odolnost proti chybám
- Řízení katalogu dat a paměti