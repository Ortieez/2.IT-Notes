### Co je UNIX?

- UNIX je ochranná známka operačního systému, který byl vytvořen firmou AT&T v roce 1969 (Ken Thompson a Dennis Ritchie v Bell Laboratories).

- Ochrannou známku vlastní konsorcium The Open Group.

- UNIX vychází ze systému Multics.

- UNIX je napsán v programovacím jazyce C.

- Existuje velké množství různých variant a klonů OS UNIX více či méně kompatibilních.


### Typy Unix-like OS
- AIX – Verze Unixu, vyvinutá firmou IBM pro její řadu RISCových počítačů RS/6000
- BSD
- FreeBSD
- OpenBSD
- NetBSD
- DragonFly BSD
- HP-UX
- Tru64
- IRIX
- GNU/Linux
- Mac OS X
- Solaris

### Architektura UNIX

![[Architektura UNIX.png]]

### Vlastnosti OS UNIX 
- Víceúlohový
- Víceuživatelský
- Unifikované prostředí
- Hierarchický systém souborů
- Vše je soubor
- Podpora práce v síti
- Grafické prostředí
- Rozšíření pro práci v reálném čase
- Podpora multiprocesorových systémů

#### [[Obvyklá struktura adresářů]]
#### [[Rozdělení Souborů]]

### Přístupová práva
- Každý obyčejný soubor a adresář má tyto atributy:
	- Jméno souboru
	- Jedinečné číslo i-uzlu
	- Vlastníka
	- Čas posledního přístupu
	- Čas poslední modifikace
	- Čas poslední změny i-uzlu
	- Počet odkazů na soubor z adresářů (počet linků)
	- Velikost souboru v bytech.
	   
- Soubory mohou být před nežádoucím přístupem chráněny nastavením přístupových práv.

- Každému souboru lze nastavit přístupová práva pro čtení, zápis nebo vykonávání pro vlastníka, skupinu nebo všechny.