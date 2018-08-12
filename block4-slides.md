# Block 4: kleine Skripte

## VS Code einrichten

* Windows-Startmenu aufrufen
* unter 'A': Anaconda auswählen
* Anaconda Navigator anklicken
* VS Code installieren

## VS Code starten

* Windows-Startmenu aufrufen
* unter 'A': Anaconda auswählen
* Anaconda-Prompt anklicken
* 'code' eingeben

## Python Extension einbinden

* ganz links viertes Symbol von oben klicken
* im Suchfeld 'Python' eingeben
* ersten Treffer auswählen und installieren
* Code neu starten

## Python-Datei anlegen

* speichern unter: Dateiname eingeben
* Dateiendung: .py anhängen

## User-Input Skript

```Python
# Eingabe Name
name = input("Wie heißt du? >>>")
# Eingabe Alter
alter = input("Wie alt bist du? >>>")
# Eingabe Wohnort
ort = input("Wo wohnst du? >>>")
jahr = 2018 - int(alter)
# Ausgabe
print(f"""
\nHallo {name}, schön, dass du da bist!\n
Du bist {jahr} geboren.\n
{ort} ist der beste Ort auf dem Planet.""")
```

## Skript aufrufen

* STRG + ö
* ins Verzeichnis navigieren
* python DATEINAME.py

## Anweisungsaufbau und Einrückungen

ANWEISUNGSKOPF:**DOPPELPUNKT**

**EINRÜCKUNG** ANWEISUNG

## Fehlerbehandlung / error handling

```Python
for x in range

  File "<ipython-input-1-a89b35aad551>", line 1
    for x in range
                  ^
SyntaxError: invalid syntax
```

## help() Function

```Python
help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```

## Juypter Notebooks einrichten

* Windows-Startmenu aufrufen
* unter 'A': Anaconda auswählen
* Anaconda Navigator anklicken
* Jupyter Lab installieren

## Jupyter Lab starten

* Windows-Startmenu aufrufen
* unter 'A': Anaconda auswählen
* Anaconda-Prompt anklicken
* 'juypter lab' eingeben

## Jupyter Notebook starten

* ganz links 'Files' klicken
* in das Arbeitsverzeichnis navigieren
* im Launcher Notebook Python 3 auswählen

## Jupyter Notebook Short Cuts

* STRG + Eingabe: = Zelle ausführen
* B = neue Zelle unten einfügen

## Kontrollstrukturen

## For-Schleife

```Python
for x in range(10):
    print(x)
```

## While-Schleife

```Python
x = 10
while x > 0:
    print(x)
    x -= 1
```

## If-Anweisung

```Python
for x in range(1, 11):
    if x % 2 == 0:
        print(f"{x} ist eine gerade Zahl.")
    else:
        print(f"{x} ist eine ungerade Zahl.")
```

## Dateien lesen und schreiben

```Python
f = open("DATEI.txt", "r", encoding="utf-8")
grundgesetz = f.read()
f.close()

with open("DATEI.txt", "w", encoding="utf-8") as f:
    f.read()
```

## I/O Parameter

* "r" = lesen
* "w" = schreiben
* "a" = append / anhängen