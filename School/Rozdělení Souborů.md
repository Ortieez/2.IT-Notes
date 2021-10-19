# Rozdělení Souborů

### Obyčejné soubory
- To, co běžně míníme pojmem soubor. 
- Obyčejné soubory mohou obsahovat texty, binární data, spustitelné programy, …

### Adresářové soubory
- Soubory přípustné pouze pro čtení
- Obsahují informace o souborech umístěných v adresáři
- Pro každou položku v adresáři se tato informace skládá ze jména souboru a čísla i-uzlu (**inode number**)

- Každému objektu (souboru) odpovídá právě jeden i-uzel
- Jedná se o metadata obsahující informace o souboru
	- Například:
		- Typ souboru
		- Kdo je vlastníkem
		- Přístupová práva
		- Počet odkazů
		- Velikost
		- Časové informace

### Speciální soubory
- Odpovídají fyzickým zařízením

	- Jako jsou: 
		- Pevné disky
		- Disketové mechaniky
		- Terminály
		- Tiskárny nebo paměť

- Speciální soubory jsou umístěny v adresáři /dev. Speciální soubory jsou buď blokové (hdd, ...) nebo znakové (terminály, tiskárny, ...)