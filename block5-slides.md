# Textanalyse mit Python

## Textanalyse mit Python 

Python ist für die Arbeit mit Texten gut geignet,
dabei helfen *libraries* wie:

* NLTK, gensim, pattern, textblob, spacy

## Buchempfehlung

Steven Bird, Ewan Klein, Edward Loper,

Natural Language Processing with Python

– Analyzing Text with the Natural Language Toolkit, O'Reilly Media, 2009 *[updated to Python 3 and NLTK 3]*.

Online:

[http://www.nltk.org/book/](http://www.nltk.org/book/)

## Textanalyse mit Python

Tutorial unter:
[http://www.karsdorp.io/python-course/](http://www.karsdorp.io/python-course/)

# Block 5: eigene Funktionen schreiben

## Vorbereitung

* [https://www.bundestag.de/gg](https://www.bundestag.de/gg)
* Text kopieren
* Texteditor aufrufen und Text einfügen
* speichern als: grundgesetz.txt
* speichern mit UTF-8-Codierung
* Speicherort: Arbeitsverzeichnis

## Web Scraping

```Python
import requests
from bs4 import BeautifulSoup

url = "https://www.bundestag.de/gg"
response = requests.get(url)
html = response.text
```

## Web Scraping

```Python
soup = BeautifulSoup(html, "html.parser")
html_text = soup.find(attrs={"class": "bt-standard-content"})
text = html_text.get_text()

with open("grundgesetz.txt", "w", encoding="utf-8") as infile:
    infile.write(text)
```

## Text aus Datei einlesen

```Python
infile = open("grundgesetz.txt", encoding="utf-8")
text = infile.read()
infile.close()
```

## Text vorbereiten

```Python
def remove_punc(text):
	punctuation = "!@#$%^&*()_*+={}[]:;"\'|,.?/~"
	for marker in punctuation:
	    text = text.replace(marker, "")
	return text
```

## Text säubern

```Python
def clean_text(text):
	return remove_punc(text.lower())

text = clean_text(text)
```

## Wörter zählen

```Python
text.count("gesetz")
```

## Wörter zählen

```Python
words = text.split()
print(len(words))
print(words[:100])
```

## Funktion Wörter zählen

```Python
def count_in_list(item_to_count, list_to_search):
	number_of_hits = 0
	for item in list_to_search:
		if item == item_to_count:
		    number_of_hits += 1
	return number_of_hits

print(count_in_list("freiheit", words))
```

## Funktion Wörter zählen

```Python
for word in words[:100]:
	print(word, count_in_list(word, words))
```

## Funktion Wörter zählen

```Python
def counter(list_to_search):
	unique_words = set(list_to_search)
	for word in unique_words:
		print(word, count_in_list(word, list_to_search))

counter(words)
```

## Wörter zählen mit dictionary

```Python
def counter_dict(list_to_search):
	counts = {}
	for word in list_to_search:
		if word in counts:
		counts[word] = counts[word] + 1  
		else:
		counts[word] = 1
	return counts
```

## Ergebnis in Datei schreiben

```Python
frequency_distribution = counter_dict(words)

outfile = open("gg-worte.txt", "w", encoding="utf-8")

for word, frequency in frequency_distribution.items():
	outfile.write(word + ";" + str(frequency) + '\n')

outfile.close()
```

## Worthäufigkeiten sortieren

```Python
def freq_count(list_to_search):
	counts = counter_dict(list_to_search)

	return ([(k, counts[k]) for k in
	sorted(counts, key=counts.get, reverse=True)])

print(freq_count(words)[:50])
```

## Ergebnis in Datei schreiben

```Python
frequency_distribution2 = freq_count(words)

outfile = open("gg-worte2.txt", "w", encoding="utf-8")

for word, frequency in frequency_distribution2:
	outfile.write(word + ";" + str(frequency) + '\n')

outfile.close()
```

## Vorbereitung Stoppwörter entfernen

* [http://members.unine.ch/jacques.savoy/clef/germanST.txt](http://members.unine.ch/jacques.savoy/clef/germanST.txt)
* Text kopieren
* Texteditor aufrufen und Text einfügen
* speichern als: stopwords.txt
* speichern mit UTF-8-Codierung
* Speicherort: Arbeitsverzeichnis

## Stoppwörter entfernen

```Python
def remove_stopwords(list_to_search):

	infile = open("stopwords.txt", encoding="utf-8")
	stopwords = infile.read()
	infile.close()
	stopwords = stopwords.split()

	return [w for w in list_to_search if w not in stopwords]

clean_words = remove_stopwords(words)
```

## Ergebnis in Datei schreiben

```Python
frequency_distribution3 = freq_count(clean_words)

outfile = open("gg-worte3.txt", "w", encoding="utf-8")

for word, frequency in frequency_distribution3:
	outfile.write(word + ";" + str(frequency) + '\n')

outfile.close()
```