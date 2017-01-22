# -*- coding: utf-8 -*-
"""
Author: https://github.com/mayankshekhar03

"""
import requests
from bs4 import BeautifulSoup as bs

def tv_series_url_list(max_pages):
    page = 1
    f = open("tv_series_name.html","w+")
    f.write("<html>\n<body>\n")
    while page <= max_pages:
        url = "http://tv/series/parent/directory" + "s" + str(page) + "/"
        scode = requests.get(url)
        plaintext = scode.text
        soup = bs(plaintext, "lxml")
        for link in soup.find_all('a'):
            if 'media file type' in link.get('href'):
                href = "http://tv/series/parent/directory" + "s" + str(page) + "/" + link.get('href')
                title = link.string
                with open('tv_series_name.html', 'a') as myfile:
                    myfile.write('<a href="'+href+'">'+title+'</a><br>\n')
                #print(title)
                #print(href)
        page += 1
    with open('tv_series_name.html', 'a') as myfile:
        myfile.write('</body>\n</html>')

tv_series_url_list(number of seasons)
