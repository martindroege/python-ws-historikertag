#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Scraping Hsozkult.de """
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = "http://www.hsozkult.de"
query_string = "/searching/page?q="
search_string = "rezension grundwissenschaft"
search_string = search_string.replace(" ", "+")
url = base_url + query_string + search_string

search = urlopen(url)
bs = BeautifulSoup(search, 'html.parser')

results = bs.find_all('div', {'class': 'hfn-list-itemtitle'})

first_hit = results[0].find('a')['href']

link_url = base_url + first_hit
link_url = link_url.replace(" ", "%20")

review_html = urlopen(link_url)
bs_review = BeautifulSoup(review_html, 'html.parser')

meta_data = {}

for key, val in bs_review.find_all('div', {'class': 'hfn-item-metarow'}):
    k = key.get_text()
    k = k.strip()
    v = val.get_text()
    v = v.strip()
    v = re.sub(r"[\n\t]+", " ", v)
    if k != '':
        meta_data[k] = v

review_author = bs_review.find('div', {'class': 'hfn-item-creator'})
review_author = review_author.get_text()
review_author = review_author.strip().split(',')[0]

review = bs_review.find('div', {'class': 'hfn-item-fulltext'}).find_all('p')

review_content = [paragraph.get_text() for paragraph in review]

with open('rezension.txt', 'w', encoding='utf-8') as f:
    if 'Hrsg. v.' in meta_data.keys():
        f.write("{}: Rezension von: {} (Hg.): {}, {}.".format(
            review_author,
            meta_data['Hrsg. v.'],
            meta_data['Titel'],
            meta_data['Erschienen']))
    else:
        f.write("{}: Rezension von: {}: {}, {}.".format(
            review_author,
            meta_data['Autor(en)'],
            meta_data['Titel'],
            meta_data['Erschienen']))
    f.write("\n\n")
    f.write("\n".join(review_content))
