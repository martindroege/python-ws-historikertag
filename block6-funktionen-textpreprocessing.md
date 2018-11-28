# Block 6: eigene Funktionen schreiben - Textpreprocessing

## Text-Datei einlesen

```python
with open("DATEINAME.txt", encoding="utf-8") as infile: 
    rezension = infile.read()
```

## Kleinschreibung vereinheitlichen

```python
def text_lower(text):
    return text.lower()

rezension = text_lower(rezension)
print(rezension[:250])
```

## Punktation entfernen

```python
import string

def remove_punctuation(text):
    punctuation = string.punctuation
    for marker in punctuation:
        text = text.replace(marker, "")
    return text

rezension = remove_punctuation(rezension)
print(rezension[:250])
```

## Liste erstellen

```python
rezension_words = rezension.split()
```

```python
print("Anzahl aller Worte des Textes: ", (len(rezension_words)))
print("=======")
print(rezension_words[:25])
```

## Zählen eines bestimmten Worts

```python
def count_item_in_text(item_to_count, list_to_search): 
    number_of_hits = 0                            
    for item in list_to_search:                   
        if item == item_to_count:                 
            number_of_hits += 1                   
    return number_of_hits 

print(count_item_in_text("information", rezension_words))
```

## Alle Wörter zählen mit Hilfe eines Dictionarys

```python
def counter_dict(list_to_search):                 
    counts = {}                              
    for word in list_to_search:              
        if word in counts:                   
            counts[word] = counts[word] + 1  
        else:                                
            counts[word] = 1                 
    return counts

print(counter_dict(rezension_words))
```

## Worthäufigkeiten sortieren

```python
def freq_sort(list_to_search):       
    counts = counter_dict(list_to_search)
    counts = [(counts[key], key) for key in counts]
    counts.sort()
    counts.reverse()
    return counts

print(freq_sort(rezension_words)[:25])
```

## Entfernen von Stoppwörtern

```python
import requests

def remove_stopwords(list_to_search):
    stopword_url = "http://members.unine.ch/jacques.savoy/clef/germanST.txt"
    response = requests.get(stopword_url)
    stopwords = response.text
    stopwords = stopwords.split()
    return [w for w in list_to_search if w not in stopwords]
  
print(remove_stopwords(rezension_words))
```

## Funktionsaufrufe

```python
rezension = text_lower(rezension)
rezension = remove_punctuation(rezension)
rezension_words = rezension.split()
rezension_words = remove_stopwords(rezension_words)
print(freq_count(rezension_words)[:25])
```
