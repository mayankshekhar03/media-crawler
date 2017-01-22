# -*- coding: utf-8 -*-
"""
Author: https://github.com/mayankshekhar03

"""
import requests
from bs4 import BeautifulSoup as bs

def tv_series_url_list(max_pages):
    page = 1
    f = open("new_girl.html","w+")
    f.write("<html>\n<body>\n")
    while page <= max_pages:
        url = "http://s1.bia2m.biz/Series/New%20Girl/" + "s" + str(page) + "/"
        scode = requests.get(url)
        plaintext = scode.text
        soup = bs(plaintext, "lxml")
        for link in soup.find_all('a'):
            if 'New Girl' in link.string:
                href = "http://s1.bia2m.biz/Series/New%20Girl/" + "s" + str(page) + "/" + link.get('href')
                title = link.string
                with open('new_girl.html', 'a') as myfile:
                    myfile.write('<a href="'+href+'">'+title+'</a><br>\n')
                #print(title)
                #print(href)
        page += 1
    with open('new_girl.html', 'a') as myfile:
        myfile.write('</body>\n</html>')

tv_series_url_list(7)