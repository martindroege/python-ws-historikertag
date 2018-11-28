# Block 6b: NLTK

## collections

```python
import collections

freq = collections.Counter(text)
```

## most common

```python
print(freq.most_common(25))
```

## remove punctation

```python
import string

def remove_punctuation(text):
    punctuation = string.punctuation
    for marker in punctuation:
        text = text.replace(marker, "")
    return text
```

# NLTK

```python
import nltk

with open("grundgesetz.txt", encoding="utf-8") as infile:
    text_raw = infile.read()

text = text_raw.lower()
text = remove_punctuation(text)
text = text.split()
text = nltk.Text(text)
```

## concordance

```python
text.concordance("freiheit")
```

## similar

```python
text.similar("freiheit")
```

## dispersion plot

```python
text.dispersion_plot(["artikel", "gesetz", "freiheit"])
```

## NLTK-Beispiel

(aus: http://www.nltk.org/book/ch02.html)


```python
import nltk
from nltk.corpus import inaugural

cfd = nltk.ConditionalFreqDist(
          (target, fileid[:4])
          for fileid in inaugural.fileids()
            for w in inaugural.words(fileid)
               for target in ['america', 'citizen']
                   if w.lower().startswith(target))
cfd.plot()
```
