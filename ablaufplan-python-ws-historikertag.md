# Entwurf Ablaufplan Python-Workshop Historikertag

## Vorfeld

* Email an TN schreiben
  * Anleitung und Links für
    * Installation Anaconda
    * Installation VS Code als Editor (wird mit dem neuen Anaconda ausgeliefert; VIM-Keybindings sind möglich!)

## am Tag des Workshops

* ab 13 Uhr Unterstützung bei:
  * Installation
  * Arbeitsumfeld
  * sonstigen Problemen

## Block 0: Vogeplänkel

* Dauer: 15 Minuten

* Vorstellungsrunde
* Erwartungen
* Zeitplan
* Vorgehen
* Ziele: Warum Programmieren für Historiker?
* Grenzen
* Fragen erlaubt!
* Verteilung der ausgedruckten Anleitungen
* zwei 'Lern-Stränge' erläutern:
  * Selbst coden: Lernen beim Tun
  * Benutzung der Tools zum Coden: Kennenlernen der Arbeitsumgebung
    * Kommandozeile
    * IPython
    * Notebooks
    * Editoren (VS Code)
    * Anaconda / Conda
    * PIP install (?)
    * Module
    * Dokumentationen

## Block 1: Vorbereitung

* Dauer: 20 Minuten

### a) Historie, Konzept, Einsatzgebiete

* lesbare Syntax
* Rapid Prototyping
* OOP
* Community
* Unterschiede 2.7 vs 3.x
* erste Programmierprinzipien:
  * Dopplung vermeiden

### b) Arbeitsumfeld einrichten und erläutern

* Arbeitsverzeichnis
  * Ordnerstruktur
  * Projektstruktur
* wissenschaftliche Arbeitsumgebung Anaconda
  * conda Package-Manager
  * env einrichten, um Paket-Konflikte zu vermeiden
* Editor einrichten
  * Bedeutung und Nutzen

### c) Hilfe zur Selbsthilfe

* Links
* Tutorials
* Stackoverflow
* Dokumentationen
* Hilfe in Anaconda
* Bücher

## Block 2: Erste Schritte

* Dauer: 10 Minuten

### a) Python-Interpreter und IPython

* Terminal / Anaconda-Prompt starten
* Python-Version
* Syntax Highlighting
* erweiterte Funktionen
* Kommandozeilen-Einbindung
* Magische Befehle
* Vorteil und Nutzen
* print("Hallo Welt!")

### b) Ganze Zahlen und Operatoren

* Rechenoperationen durchführen
* Pfeiltasten für History

### c) Gleitkommazahlen

* Rechenoperationen durchführen
* Unterschied 2.7 und 3.x

## Block 3: Datentypen

* Dauer: 30 Minuten


### a) Zeichenketten / Strings

* Konkatenieren
* Speichern in Variablen
* Interpolieren f" " und .format
* built-in-Funktionen / Methoden bei Strings
  * len() etc.
  * .lower etc.
* Unterschied 2.7 und 3.x (für Strings)

### b) Listen / lists

* Methoden
  * sort()
  * append() etc.
* Indexieren
  * auch bei Strings und sequenziellen Datentypen
* Slicing
* Listen von Listen

### c) Zuordnungen / dictionaries

* Schlüssel-Wert-Paare
* Zugriff auf key, value
* Vorteil und Nutzen

### d) Unveränderbare Listen
* tuple
* set

### e) Logische Ausdrücke

* Wahrheitswerte True / False
* Vergleichsoperatoren
* and / not / or

## **kurze Pause: 10 Minuten**

## Block 4: kleine Skripte

* Dauer: 30 Minuten

### a) Editor nutzen

* VS Code: Python Extension installieren
* .py speichern im Arbeitsverzeichnis
* Terminal starten und .py aufrufen

### b) Grundlegendes

* Anweisungskopf und Anweisung
* Einrückungen / Intendation
* Kommentare (auch zur Dokumentation in der Datei)
* Umbrechen langer Zeilen \
* Fehlerfall / errors
  * Backtrace / Fehler leicht zu identifizieren
* Function help()

### c) Jupyter Notebooks und Literate Programming (das könnte länger dauern!)

* Jupyter Lab einrichten und starten
* Vorteile und Nutzen
* grundlegende Funktionalität erläutern
* ... ab jetzt im Notebook?

### d) Kontrollstrukturen

* if-Anweisungen
* while-Schleifen
* for-Schleifen

### e) aus Dateien lesen und schreiben / I/O

* with open() as:
* encoding als parameter
* w, r, a als parameter

## Block 5: eigene Funktionen schreiben

* Dauer: 30 Minuten

### a) Funktionen selber schreiben

* Aufbau
* Aufruf
* Parameter und Argumente
* Namensräume
* Nutzen und Vorteile

### b) Funktionen für Text-Preprocessing

* siehe textpyprocess(?)
* read_text
* remove_punctation
* remove_stopwords
* count_frequencies
* sortieren etc.

### c) Module / Bibliotheken

* vorstellen NLTK etc.
* import
* Aufruf

## **große Pause: 25 Minuten**

## Block 6: Skript-Projekt

* Dauer: 60 Minuten, Pausen nach Bedarf

### a) Projekt: Suchen und Ersetzen? Wortwolken?

### (b) Projekt: Web-Scraping)

* Scraping von Blogs bei hypotheses
* ausgetestet: sehr aufwändig!
* besser nur auf ein Projekt konzentrieren!
* Scraping von Hsozkult oder Wikipedia?

## Block 7: Selbsthilfe

* Dauer: 10 Minuten

### a) nächste Schritte

* Links / Tutorials / Bücher empfehlen

### b) offene Fragen klären

### c) kurze Feedback-Runde

## **gemeinsames Abendessen**

* Tisch reservieren