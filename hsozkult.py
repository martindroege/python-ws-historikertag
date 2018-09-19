#!/usr/bin/env python

""" Scraping Hsozkult.de """
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.hsozkult.de/publicationreview/id/rezbuecher-26978')
bs = BeautifulSoup(html, 'html.parser')

meta = bs.find('div', {'class': 'hfn-item-meta'})

meta_data = {}

for key, val in meta.find_all('div', {'class': 'hfn-item-metarow'}):
    k = key.get_text()
    k = k.strip()
    v = val.get_text()
    v = v.strip()
    v = re.sub(r"[\n\t]+", " ", v)
    if k != '':
        meta_data[k] = v


review_author = bs.find('div', {'class': 'hfn-item-creator'})
review_author = review_author.get_text()
review_author = review_author.strip().split(',')[0]

review = bs.find('div', {'class': 'hfn-item-fulltext'}).find_all('p')

review_content = []

for paragraph in review:
    review_content.append(paragraph.get_text())

if 'Hrsg. v.' in meta_data.keys():
    print("{}: Rezension von: {} (Hg.): {}, {}.".format(review_author,
                                                        meta_data['Hrsg. v.'],
                                                        meta_data['Titel'],
                                                        meta_data['Erschienen']))
else:
    print("{}: Rezension von: {}: {}, {}.".format(review_author,
                                                  meta_data['Autor(en)'],
                                                  meta_data['Titel'],
                                                  meta_data['Erschienen']))
print()
for para in review_content:
    print(para)
