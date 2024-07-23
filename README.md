## 1. OBECNÝ POPIS PROGRAMU
Tento program, nazvaný "neOpisuj_1.0", umožňuje na základě analýzy slovosledu textových řetězců porovnávat míru shodnosti dvou textů; takových, o kterých panuje důvodná obava, že jeden je plagiátem druhého.
Má být zejména pomůckou pro právníky, ale stejně tak nalezne uplatnění třeba i ve školství nebo pří pořádání vzdělávacích kursů; zkrátka všude tam, kde je třeba kontrolovat, zda nedocházelo k opisování. 
V právní praxi se zejména uplatní v případech, kdy je zřejmé, že odůvodnění rozhodnutí soudu nebo nějakého orgánu veřejné správy bylo metodou CTRL+C, CTRL+V zkopírováno z podání některé ze stran. 
Takové zjištění není bezvýznamné: občanský soudní řád, který upravuje postup soudu v občanskoprávních řízeních jako je třeba rozvod, žaloby na neplatnost smluv a podobně, výslovně zakazuje, 
aby soudy v odůvodnění svých rozhodnutích opisovaly to, co ve svých podáních uvádí strany. Pokud se tak stane, takový rozsudek lze napadnout odvoláním pro jeho tzv. nepřezkoumatelnost a odvolací soud jej zruší
a soudu prvního stupně uloží, aby věc znovu projednal. Obdobně je tomu v řízení trestním nebo v řízení před jinými veřejnými orgány, třeba před finančním nebo stavebním úřadem. 

Aby ale argumentace tzv. nepřezkoumatelností rozhodnutí měla reálný základ, je potřeba ji odůvodnit nějakým ověřitelným způsobem. Tím je zde program, jenž využívá jednoduchou metodu zpracování přirozeného jazyka (NLP)
pro analýzu textových dat. Ten, jak již bylo řečeno, neporovnává shodnost použitých slov, ale slovosledu. To znamená, že pokud jeden text obsahuje větu „Honza jde do lesa“ a druhý „Do lesa jde Honza“, 
program je nevyhodnotí jako shodné a bude je ignorovat. Jako shodné je zhodnotí pouze tehdy, pokud shodný bude slovosled, tedy pokud oba texty budou identické. 

Po uživatelské stránce platí, že do programu nejprve vkládáme první a poté druhý ze sporných textů (například příslušný odstavec rozsudku a poté týž odstavec žaloby, odstavec práce jednoho žáka a poté druhého). 
Hovoříme zde tak o dvojici textů. Poté provedeme jejich porovnání. Nejprve se zobrazí nejprve text, který je vytvořen ze shodných textových řetězců. Dalším údajem je míra shodnosti obou textů v procentech. 
Pokud vkládáme více sporných dvojic textů, program dále zaznamená jak počet porovnaných párů, tak údaje další, a to již statistické povahy: 
-	průměrnou procentuální míru shodnosti všech zkoumaných dvojic, 
-	minimální a maximální  míru shodnosti, jakož i 
-	medián a kvartily
Tyto všechny údaje mají svůj význam. Pokud minimální hodnota shodnosti bude  > 0, jen trochu rétoricky zdatný právník prohlásí, že v odůvodnění rozsudku nenalezneme text,
který by nebyl v té či oné míře kopií podání jedné ze stran. Pokud 1. kvartil bude činit > 50%, je korektní tvrdit, že tři čtvrtiny zkoumaného textu jsou více jak z poloviny plagiátem,
pokud medián bude činit > 75%, je obdobně korektní tvrdit, že  polovina všeho textu odůvodnění je dokonce ze tří čtvrtin plagiátem, a podobně. Analogickým způsobem může argumentovat jakýkoliv vyučující nebo školitel.
Konečně, uložené údaje jsou vkládány do SQL databáze pro další použití. Z důvodu ochrany osobních údajů je pak lze kdykoliv příslušným příkazem vymazat. 

## 2. ARCHITEKTURA PROGRAMU
# 2.1 Obecný popis
Tento progam je vytvořen na bázi OOP. Je navržen pro analýzu textových dat a je postaven na následujících hlavních komponentách:

  1. **Správa databáze**: Soubor **database_manager.py** obsahuje třídu DatabaseManager, která poskytuje metody pro vytváření tabulek, vkládání a načítání dat z databáze SQLite.
  2. **Grafické uživatelské rozhraní (GUI)**: Soubor **gui_app.py** obsahuje třídu GUIApp, která vytváří GUI aplikaci pomocí Tkinter.
   Uživatelé mohou zadávat data prostřednictvím GUI, která jsou následně uložena do databáze.
  3. **Instalace balíčků**: Soubor **install_dependencies.py** poskytuje skript pro instalaci potřebných Python balíčků.
  4. **Analýza textu**: Soubor **text_analysis.py** obsahuje funkce pro analýzu textových dat, zejména pro počítání frekvence slov v textu.
  5. **Databázový soubor**: Soubor **results.db** je databázový soubor SQLite, který ukládá výsledky analýzy a
  6. **Projektový soubor**: Soubor **results.sqbpro** je projektový soubor pro správu této databáze pomocí externího nástroje.
   
# 2.2 Metoda použitá v programu
Tento program využívá jednoduchou metodu zpracování přirozeného jazyka (NLP) pro analýzu textových dat. Postup je následující:
  1. **Odstranění interpunkce**: Text je očištěn od veškeré interpunkce, aby byla zajištěna čistota dat.
  2. **Konverze na malá písmena**: Všechna písmena v textu jsou převedena na malá, což umožňuje jednotné zpracování a počítání slov bez ohledu na jejich původní velikost.
  3. **Tokenizace**: Text je rozdělen na jednotlivá slova (tokeny), což je nezbytné pro další analýzu.
  4. **Počítání frekvence slov**: Pomocí třídy `Counter` z modulu `collections` je spočítána frekvence výskytu každého slova v textu.

Tato metoda umožňuje efektivní analýzu textových dat a získání přehledu o nejčastěji používaných slovech v analyzovaném textu.

# 2.3 Jednotlivé moduly programu
# 2.3.1 Správa databáze
Soubor database_manager.py obsahuje:
  1. třída DatabaseManager
  2. Metody:
  __init__(self, db_name): Inicializuje připojení k databázi s názvem db_name.
  create_table(self, create_table_sql): Vytvoří tabulku podle zadaného SQL příkazu.
  insert_data(self, table, data): Vloží data do specifikované tabulky.
  fetch_data(self, query): Načte data z databáze na základě zadaného SQL dotazu.
  close_connection(self): Uzavře připojení k databázi.


# 2.3.2. Grafické uživatelské rozhraní
Soubor gui_app.py obsahuje třídu GUIApp, která vytváří grafické uživatelské rozhraní (GUI) pomocí Tkinter.

  # 2.3.2.1 Atributy:
  root: Hlavní okno Tkinter aplikace.
  db_manager: Instance třídy DatabaseManager pro správu databáze.

  # 2.3.2.2 Metody:
  __init__(self, root): Inicializuje GUI aplikaci.
  setup_ui(self): Nastaví uživatelské rozhraní.
  submit_data(self): Zpracuje a uloží zadaná data.


# 2.3.3. Instalace balíčků
Soubor install_dependencies.py slouží k automatické instalaci Python balíčků pomocí pip. 
Pomocí modulu subprocess volá příkaz pip install pro každý balíček uvedený v seznamu packages.

  # 2.3.3.1 Funkce install(package):
  Používá subprocess.check_call k provedení příkazu pip install pro zadaný balíček.
  Příkaz je proveden s aktuálním Python interpretem (sys.executable).

  # 2.3.3.2 Seznam balíčků:
  Obsahuje názvy balíčků, které mají být nainstalovány. V základní verzi obsahuje balíčky tk, sqlite3 a collections, 
  které jsou součástí standardní knihovny Pythonu a není nutné je instalovat pomocí pip.

  # 2.3.3.3 Hlavní část skriptu:
  Pro každý balíček v seznamu packages volá funkci install(package) a instaluje jej.


# 2.3.4. Analýza textu
Soubor TextAnalyzer je třída pro analýzu textových dat. Poskytuje metody pro načítání, předzpracování a analýzu textu, 
včetně počítání frekvence slov.

  # 2.3.4.1 Hlavní metody:
    load_text(self, text): Načte text pro analýzu.
    preprocess_text(self): Odstraní interpunkci a převede text na malá písmena.
    analyze_text(self): Předzpracuje text a spočítá frekvenci slov.
    get_most_common_words(self, n=10): Vrátí seznam nejčastějších slov.
    get_word_count(self): Vrátí Counter s frekvencí všech slov.


# 2.3.5. Databázový soubor
Soubor results.db je databázový soubor SQLite, který slouží k ukládání výsledků analýzy textu. 
Tento soubor je spravován pomocí třídy DatabaseManager ze skriptu database_manager.py - viz kapitola # 2.3.1.

  # 2.3.5.1 Základní popis
    Typ souboru: SQLite databázový soubor
    Účel: Ukládání a správa dat zadaných a analyzovaných prostřednictvím GUI aplikace
    Správa: Interakce s databází je zajištěna třídou DatabaseManager v database_manager.py

  # 2.3.5.2 Struktura databáze
    Předpokládaná struktura tabulky v databázi může být následující (na základě použití v GUI aplikaci):
    Tabulka results:
    Sloupce:
      id: Primární klíč, automaticky se inkrementuje
      data: Textová data zadaná uživatelem

  # 2.3.5.3 Správa databáze
    Pro správu databáze lze využít jakýkoliv SQLite nástroj, například DB Browser for SQLite, 
    který umožňuje prohlížení a úpravu obsahu databázového souboru results.db.



# 2.3.6. Projektový soubor
Projektový soubor results.sqbpro` je  soubor pro DB Browser for SQLite, který ukládá konfiguraci a nastavení specifická pro projekt.
Tento soubor slouží k usnadnění správy databáze `results.db`. Ukládá informace o:
  - Otevřených databázových souborech
  - SQL dotazech
  - Záložkách
  - Dalších nastaveních specifických pro projekt
Při správě databáze results.db lze použít DB Browser for SQLite a otevřít soubor results.sqbpro pro rychlý přístup ke všem nastavením a konfiguracím, 
které jsme předtím vytvořili. Tento soubor není nutný pro běh samotného programu, ale slouží pro vývoj a správu databáze během vývoje aplikace.



## 3. INSTALACE PROGRAMU
# 3.1 Otevření projektu v PyCharm:
Spusťte PyCharm.
Klikněte na File -> Open a vyberte složku obsahující všechny nahrané soubory.

# 3.2 Instalace balíčků:
Otevřete soubor install_dependencies.py v PyCharm.
Klikněte pravým tlačítkem na soubor a vyberte Run 'install_dependencies' pro instalaci potřebných balíčků.

# 3.3 Příprava databáze:
Ujistěte se, že soubor results.db je ve stejné složce jako ostatní skripty.

# 3.4 Spuštění GUI aplikace:
Otevřete soubor gui_app.py v PyCharm.
Klikněte pravým tlačítkem na soubor a vyberte Run 'gui_app'.
Tím se spustí GUI aplikace, kde můžete zadávat textová data a ukládat je do databáze.

# 3.5 Použití TextAnalyzer:
Otevřete soubor text_analysis.py a můžete jej spustit samostatně pro analýzu textu.



## 4. PRAKTICKÉ POUŽITÍ APLIKACE
# 4.1 Textové formáty
Aplikace podporuje textové formáty, jako jsou HTML, Markdown, Word dokumenty, CSV a PDF. 

# 4.2 Před vkládáním textu
Před každým novým vkládáním textu je vhodné nejprve stisknout tlačítko "Vymazat záznamy". 
Tím se předejde nebezpečí, že aplikace bude i nadále kalkulovat s již předtím zpracovávanými daty.

# 4.3 První vložení textu
Aplikace obsahuje ve své horní části dvě okna pro vkládání textu. Je vhodné do prvního shora vložit text
z napadeného dokumentu, do druhého původní či předchozí text, který měl být v napadeném zkopírován.

Vkládání samotné probíhá označením textu z původního zdroje (například příkazem CTRL+A nebo za pomoci myši), 
následně jeho zkopírováním buď za použití příkazu CTRL+C nebo příslušného dialogového okna a klinkutím na příkaz Kopírovat/Copy a nakonec 
vložením. To se děje buď opět za použití příkazu CTRL+V nebo příslušného dialogového okénka a klinkutím na příkaz Vložit.

Tlačítko "Porovnat texty" použijte až poté, kdy máte vloženy oba texty! Po stisknutí tohoto tlačítka proběhne analýza samotná. 
Jejím výstupem je v okénku „Shodné sekvence slov“ text, který je v obou zkoumaných dvojicích totožný. 
Míra shody je vyjádřena v okénku „Aktuální shoda v %“.

# 4.4 Další postup
Po porovnání první dvojice textů můžete buď pokračovat týmž způsobem ve vkládání dvojic, anebo můžete vkládání ukončit. 
V případě prvém použijte tlačítko „Vložit nový záznam“. Vkládací okénka se vyprázdní a lze tak vkládat novou dvojici textů. 
Zde postupujeme stejným způsobem jako při prvním vkládání.

Pokud již nechcete vkládat další dvojice, klikněte na tlačítko „Ukončit vkládání“
Poznámka! 
1.	Na tlačítko „Ukončit vkládání“ klikněte vždy před ukončením analýzy. V opačném případě se do analýzy nezapočte poslední vložený a porovnaná dvojice.
2.	Při vložení více jak jedné dvojice se objeví údaje i v dalších okénkách.

# 4.5 Ukončení analýzy
Pro ukončení analýzy postupujte následovně: 
1.	Nejprve klikněte na tlačítko „Ukončit vkládání“ Tím se do analýzy započte i poslední vložená a porovnaná dvojice.
2.	Poté klikněte na tlačítko „Ukončit program“
Protože údaje se průběžně ukládají do databáze, budete dotázán, zda si přejete )údaje uložit či nikoliv.
Pokud zvolíte možnost Ano, s údaji můžete nadále pracovat v SQL databázi. Při volbě NE se veškerá průběžně uložená data odstraní. 
