import csv
import requests
from key_name import *
from bs4 import BeautifulSoup

# csv
filename = "PoketId.csv"
f = open(filename, "w", encoding="utf-8", newline="")
writer = csv.writer(f)
# csv 타이틀
title = ['No', '이름', 'Image url']
writer.writerow(title)

# key_name 폴더에서 names 들고옴
for i in names:
    web_name = i.get_text()
    if '[1]' in web_name:
        pass
    elif '[2]' in web_name:
        pass
    elif '[3]' in web_name:
        pass
    else:
        # main web 접속
        base_url = "https://pokemon.fandom.com/ko/wiki/"
        plus_url = web_name + "_(포켓몬)"
        url = base_url + plus_url

        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")

        # 이름,no,img 변수 저장하기
        html_name = soup.find("div", attrs={"class": "name-ko"})
        text_name = html_name.get_text()
        name = text_name.replace(" ", "")

        html_no = soup.find("strong", attrs={"class": "rounded"})
        no = html_no.get_text()

        html_img = soup.find("img", attrs={"alt": "이미지"})
        imgUrl = html_img['data-src']

        # 최종 data list
        final_data = [no, name, imgUrl]
        # csv 파일 저장
        writer.writerow(final_data)
