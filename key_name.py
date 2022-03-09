import requests
from bs4 import BeautifulSoup

url = "https://ko.wikipedia.org/wiki/1%EC%84%B8%EB%8C%80_%ED%8F%AC%EC%BC%93%EB%AA%AC_%EB%AA%A9%EB%A1%9D"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

table = soup.find("table", attrs="centered aligncenter wikitable")
names = table.find_all("a")
