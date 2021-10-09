### Co je UNIX?
- UNIX je ochranná známka operačního systému, který byl vytvořen firmou AT&T v roce 1969 (Ken Thompson a Dennis Ritchie v Bell Laboratories).
- Ochrannou známku vlastní konsorcium The Open Group.
- UNIX vychází ze systému Multics.
- UNIX je napsán v programovacím jazyce C.
- Existuje velké množství různých variant a klonů OS UNIX více či méně kompatibilních.

---

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

---

### Architektura UNIX

![[Architektura UNIX.png]]

---

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

**[[Obvyklá struktura adresářů]]**
**[[Rozdělení Souborů]]**

---

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

![[Rights.png]]
![[Rights_Meaning.png]]

---

#### Změna přístupových práv
   
```bash
$ chmod [parametry] [soubor]
```

Parametry:

- u (uživatel), g (skupina), o (ostatní), a (všechny uvedené)

- \+ (přidá právo), \- (odebere právo), = (nastavení práva)

Příklady:
```bash
$ chmod a=rwx soubor
$ chmod 777 soubor

$ chmod 754 soubor
```

-  7=(111)_2→rwx=111 – pro uživatele

-  5=(101)_2→r-x=101 – pro skupinu

-  4=(100)_2→r--=100 – pro ostatní

Uživatelská práva souboru: -rwxr-xr--

Příkaz smí používat pouze root.
Nastavení práv pro soubor na vlastníka michal:
```bash
$ chown michal soubor
```

Nastavení práv pro soubor na skupinu skupina4.
```bash
$ chgrp skupina4 soubor
```

Práva zjistíme takto:
```bash
$ ls -laF
```

---

### Typ souboru

První znak označuje typ souboru:

- \- značí obyčejný soubor

- d *adresář*

- c *speciální znakový soubor*

- b *speciální blokový soubor*

- l *link neboli symbolický odkaz*

```bash
$ ln -s jméno_cíle [jméno_sym_odkazu]
```

### Základní adresářové příkazy
![[Folder_Commands.png]]

---

### Základní souborové příkazy
![[Souborove_Prikazy.png]]