#encoding:utf-8

import requests
from bs4 import BeautifulSoup

response = requests.get("https://travel.ettoday.net/article/2061711.htm")
soup = BeautifulSoup(response.text, "html.parser")

#print(soup.prettify())

result = soup.find_all("h3")
print(result)
