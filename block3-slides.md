# Block 3: Datentypen

## IPython-REPL II

* Windows-Startmenu aufrufen
* unter 'A': Anaconda auswählen
* IPython anklicken

## Navigieren im Dateiensystem

`In [1]: pwd`

`Out[1]: 'C:/Users/Martin/Documents'`

`In [2]: cd ..`

`C:/Users/Martin`

`In [3]: cd Documents`

`C:/Users/Martin/Documents`

## Magische Befehle

`%magic`

`%cpaste`

## Zeichenketten / Strings

```Python
print("Hallo Welt!")
```

## Konkatenieren

```Python
print("Hallo " + "Welt!")

print("Historikertag " + "2018")

print("Hallo " * 2 + "Historikertag")
```

## Variablen

```Python
event = "Historikertag"
year = 2018
```

## Interpolieren

```Python
print(f"Der {event} findet {year} statt.")

print("Der {} findet {} statt.".format(event, year))
```

## Funktionen und Methoden bei Strings

```Python
len(event)

len("Historikertag")

event.lower()

"Historikertag".upper()
```

## Listen / Lists

```Python
list_1 = [1, 2, 3, 4]

list_2 = ["Banane", "Apfel", "Birne"]

list_3 = [17, "Obst", 23, "Ball"]

list_4 = [[1, 2, 3,], ["a", "b", "c"], ["Hallo", "Welt"]]
```

## Zuordnungen / Dictionaries

```Python
dict_1 = {"Banane": 5, "Apfel": 7, "Birne": 9}

dict_2 = {"Vorname": "Jan", "Nachname": "Meier", "Alter": 48}
```

## Mengen / Sets

```Python
menge = {1,2,3,4,4,5,5,5}

print(menge)

type(menge)
```

## Tuple

```Python
word_freq = ("Wort A", 42)

type(word_freq)
```

## Indexieren von Strings

```Python
"Historikertag"[1]

"Historikertag"[0]

"Historikertag"[8]
```

## Slicing

```Python
"Historikertag"[0:10]

"Historikertag"[3:6]
```

## Indexieren von Listen

```Python
list_2 = ["Banane", "Apfel", "Birne"]

list_2[2]

list_2[0]
```

## Funktionen und Methoden bei Listen

```Python
len(list_2)

list_2.append("Ananas")

list_2.pop()
```

## Zugriff auf Dictionaries

```Python
dict_1 = {"Banane": 5, "Apfel": 7, "Birne": 9}

dict_1["Banane"]

dict_1.keys()

dict_1.values()

sum(dict_1.values())
```

## Logische Ausdrücke

```Python
5 > 3

5 > 7

"Mauer" == "Haus"

"Mauer" != "Haus"
```

## Logische Ausdrücke: and, or

```Python
5 > 3 and "Mauer" != "Haus"

5 > 3 and "Mauer" == "Haus"

5 > 3 or "Mauer" == "Haus"

5 > 7 or "Mauer" == "Haus"
```


