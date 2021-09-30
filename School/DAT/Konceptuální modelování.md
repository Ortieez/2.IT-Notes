- Pokus umožnit vytvoření popisu dat v databázi nezávisle na fyzickém uložení databáze.

- Měl by co nejvěrněji vystihnout konceptuální pohled člověka na danou část reálného světa.

- Limitním případem konceptuálních modelů je samotný přirozený jazyk.

### E-R konceptuální model
- Identifikuje typy entit jako třídy objektů stejného typu
	- Knihy, Předměty, Zaměstnanci, …

- Identifikuje typy vztahů mezi entitami
	- Zákazník má zapůjčenou knihu

- Typům entit a vztahům přiřazuje atributy, popisující blíže jejich vlastnosti.
	- Příjmení (údaj popisného typu) daného Zaměstnance (údaj entitního typu)

- Formuluje integritní omezení (IO), které vyjadřuje větší, či menší přesnost souladu schématu s modelovanou realitou.
	- Rodné číslo je [[Identifikační klíč|identifikačním klíčem]] entitního typu Zákazníci
	- Doménou atributu věk je množina celých kladných čísel

### Konstrukty E-R modelu
- Entita je objekt reálného světa, který je schopen nezávislé existence a je jednoznačně odlišitelný od ostatních elementů
	- Jan Kovák r.č. 123456/789

- Vztah je vazba mezi dvěma (nebo více) entitami

- Hodnota popisného typu, tedy hodnota jednoduchého datového typu
	- 123, 24.9.2007, Zeměpis, Novák, …

- Atribut určuje podstatnou vlastnost entity nebo vztahu. Použitou množinu hodnot nazveme doménou atributu.
	- Rodné číslo zaměstnance, …

