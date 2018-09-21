# Übungsaufgaben

## Block 3: Datentypen

## Übung 1

* Erstelle eine Liste.
* Die Liste soll einen String, fünf Integer und zwei Floats enthalten.
* Die Liste soll zudem ein Dictionary mit drei Key-Value-Pairs enthalten.
* Gebe über den Index den String und einen Wert aus dem Dictionary aus.

## Übung 2

* Erstelle eine Variable mit einem Namen.
* Formuliere einen Begrüßungssatz, der den Namen durch Interpolation einbindet.
* Formuliere einen Begrüßungssatz, der den Namen zweimal hintereinander durch Konkatenieren einbindet.
* Gebe beide Sätze mit print() aus.

## Block 4: Schleifen und Bedingungen

## Übung 3

* Formuliere einen kurzen Satz und weis diesen einer Variablen zu.
* Gebe die Anzahl der Buchstaben aus.
* Erstelle eine Schleife, die jeden Buchstaben des Satzes einzelnd ausgibt.
* Recherchiere die Methode split().
* Teile den Satz in Worte auf.
* Erstelle eine Schleife, die jedes Wort ausgibt.

## Übung 4

* Formuliere einen kurzen Satz und weis diesen einer Variablen zu.
* Prüfe, ob der Satz Vokale enthält.
* Gib die Anzahl der Vokale aus

# Lösungsoptionen

## Lösungsmöglichkeit für Übung 1

```Python
list_1 = ["Hallo", 1, 2, 3, 4, 5, 3.5, 4.5, \
{"first_name": "Guido", 
"last_name": "van Rossum", 
"adress": "Niederlande"}]
print(list_1[0], list_1[8]["first_name"])
```

## Lösungsmöglichkeit für Übung 2

```Python
name = "Guido"
sent_1 = f"Hallo {name}!"
sent_2 = "Hallo " + 2 * name + "!"
print(sent_1, sent_2)
```

## Lösungmöglichkeit für Übung 3

```Python
sent = "Morgen beginnt der Historikertag in Münster."
print(len(sent))
for char in sent:
    print(char)
words = sent.split(" ")
for word in words:
    print(word)
```

## Lösungsmöglichkeit für Übung 4

```Python
sent = "Morgen beginnt der Historikertag in Münster."
vowels = "aeiou"
sent = sent.lower()
number_vowels = 0
for char in sent:
    for vowel in vowels:
        if char == vowel:
            number_vowels += 1
print(number_vowels)
```