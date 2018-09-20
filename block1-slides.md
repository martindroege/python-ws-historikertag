# Block 1: Historie, Konzepte, Einsatz

## Warum Python?

* einfach zu lernen
* einfach zu lesen
* riesige Community
* laut TIOBE auf [Platz 3](https://www.zdnet.com/article/python-now-a-top-3-programming-language-as-julias-rise-speeds-up/#ftag=RSSbaffb68)
* Open Source Software

## Entwicklung

* zu Beginn der 1990er Jahre von Guido van Rossum entwickelt
* 1994 erschien die Version 1.0
* ursprünglicher Zweck: Programmieren beibringen
* Name geht nicht auf die Schlange, sondern auf Monty Python zurück
* Dezember 2008: Version 3.0 -> vollständig auf Unicode umgestellt
* Juli 2018: Guido van Rossum tritt als "Benevolent Dictator for Life" (BDFL)

## Python als Skriptsprache

Skript                      Programm          
------                      --------------------
z.B. Python                 z.B. Java oder C++                       
Interpreter                 Compiler                                 
höhere Programmiersprachen  maschinennahe Programmiersprachen        
anpassungsfähig             aufwendiger anzupassen, schwer zu debuggen

## Python als Skriptsprache

Skript                      Programm          
------                      --------------------
dynamische Typisierung      feste Typisierung                        
leichter zu erlernen        schwerer zu erlernen                 


Python-Skripte erkennbar an der Endung: `skript_name.py`


## Einsatzgebiete I

* Universitäten und Forschungseinrichtungen
* Technologie-Branche
* Industrie
* Data Science


## Einsatzgebiete II

* Data and Text Mining
* Daten-Analyse
* Visualisierung
* Web Entwicklung
* System-Administration
* Rapid Prototyping



## Arbeitsumgebung

## Das Terminal

* `cd [Verzeichnis]` - wechselt das Verzeichnis
* `cd ~` - wechselt in das Heimat-Verzeichnis
* `mkdir [Verzeichnis]` - erstellt das [Verzeichnis]
* `touch [Datei]` / `New-Item [Datei] -type file` – erstellt die [Datei]
* `rm [Datei]` - löscht (unwiederbringlich!) die [Datei]
* `rm -r [Verzeichnis]` - löscht (unwiederbringlich!) das [Verzeichnis]

## Das Terminal

* `ls` - listet den Inhalt des aktuellen Verzeichnisses auf
* `ls -lah` – wie `ls`, nur ausführlicher
* `pwd` - gibt den Namen des aktuellen Verzeichnisses an
* `man [Befehl]` - Hilfeseite zum [Befehl]
* `pydoc [keyword]` - Python-Dokumentation für [keyword]

## Arbeitsumgebung schaffen

``` shell
cd ~
mkdir Skripte
cd Skripte
```

## Anaconda

## `conda` - Package-Manager

* `conda search [Paket]` – sucht das [Paket] auf dem Server
* `conda install [Paket1] [Paket2] etc.` – installiert die Pakete
* `conda install -c conda-forge [Paket1] etc.` – installiert die Pakete von dem Server conda-forge
* `conda install -n [env] [Paket]` – installiert das Paket in die Umgebung [env]
* `conda list` – listet die Pakete auf

## `conda` - Package-Manager

* `conda update [Paket]/python/conda` – updatet [Paket], Python oder conda
* `conda remove [Paket]` – entfernt das [Paket]
* `pip3 install [Paket]` – installiert mit Pip das [Paket]


## Virtuelle Umgebungen

* `conda create -n [env]` – erschafft die Umgebung [env]
* `conda create -n [env] python=3.7` – wie oben, aber mit bestimmter Python-Version
* `conda info --envs` – Informationen zu die Umgebungen
* `conda list --explicit > spec-file.txt` – speichert die Pakete der Umgebung in [spec-file.txt]

## Virtuelle Umgebungen

* `conda install --name <env> --file spec-file.txt` – installiert genau diese Umgebung
* `activate [env]` – aktiviert die [Umgebung] auf Windows
* `source activate [env]` – aktiviert die [Umgebung] auf MacOS und Linux
* `deactivate` – deaktiviert die [Umgebung] auf Windows
* `source deactivate` – deaktiviert die [Umgebung] auf MacOS und Linux


## Editor oder IDE

* Editor: Bearbeiten von Text (Notepad++, Sublime Text, Atom, Vim, Emacs)
* IDE: Integrated Development Environment (VSCode, Eclipse, PyCharm)


## Hilfe zur Selbsthilfe

* [Python Dokumentation](https://www.python.org/doc/)
* [Python Tutorials](https://docs.python.org/3/tutorial/)
* [Programming Historian](https://programminghistorian.org/lessons/?topic=python)
* [Python Community](https://www.python.org/community/)
* [Python Forum](https://www.python-forum.de/)
* [Stack Overflow](https://stackoverflow.com/)
