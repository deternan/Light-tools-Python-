#-*- coding: utf-8 -*-

'''
version: February 19, 2022 09:58 PM
Last revision: February 19, 2022 11:02 PM

'''

import os.path
import re

from pathlib import Path
import requests
from pathlib import Path

from bs4 import BeautifulSoup


def get_description(soup):
    description_resource = soup.findAll("div", class_="description-line") or soup.findAll("div", class_="description-paragraph")
    description_content = [content.getText() for content in description_resource]
    print(description_content)

def get_classs_tag(soup):
    boldText = soup.findAll("b", class_="style-scope.patent-text")
    tag_Text = []
    for a in soup.find_all('b'):
        tag_Text.append(a.text)
        #print(a.text)
    print(tag_Text)

def main_processing():
    patent_id = "US20210341305A1"
    #patent_id = "US20210349314A1"
    url = "https://patents.google.com/patent/"
    respones = requests.get(url + str(patent_id))
    respones.encoding = 'utf-8'
    stateCode = respones.status_code
    #print(stateCode)
    if stateCode == 200:
        soup = BeautifulSoup(respones.text, "html.parser")
        #get_description(soup)
        get_classs_tag(soup)
    return stateCode



main_processing()
