import requests
from bs4 import BeautifulSoup

with open("tests.html") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
# for p in soup.find_all("p"):
#     print(p.text)

print(soup.find("body").main.p)
