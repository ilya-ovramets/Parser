import requests
from bs4 import BeautifulSoup
import random

lister = ['a','b','c','d','e','r','t','y','q','i','f','x','z','n','v','m','g','h','j','k','l','1','2','3','4','5','6','7','8','9','0']

def prefir(bigin = ''):
    i = 0
    while i < 6:
        randoms_element = random.randint(0,30)
        bigin += lister[randoms_element]
        i += 1
    return bigin


def parser():
    link = 'https://prnt.sc/'
    link = link + prefir()
    return link

def html_lib():
    try:
        url = parser()
        headers = {
            "Accept":'Encoding',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }
        req = requests.get(url, headers=headers)
        srb = req.text
        soup = BeautifulSoup(srb, 'lxml')
        skrin = soup.find('div', class_="image-container image__pic js-image-pic").find("img")
        src = skrin.get('src')
        return src
    except:
        print("url is failing")

