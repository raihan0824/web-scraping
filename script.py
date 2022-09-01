import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import string
from urllib.request import urlopen

url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/krakow?distanceRadius=0&page=1&limit=72&market=PRIMARY&locations=%5Bcities_6-38%5D&ownerTypeSingleSelect=DEVELOPER&areaMin=40&areaMax=60&viewType=listing'
soup = BeautifulSoup(urlopen(url), 'html.parser')
htmls = soup.findAll('article',{"class":"css-t1ljsh es62z2j25"})

name=[]
price=[]
pokoje=[]
area=[]
developer=[]
investment_type=[]
m2=[]
for html in htmls:
  name.append(html.find('h3').text)
  price.append(html.find('p',{"class":"css-1bq5zfe es62z2j16"}).text)
  pokoje.append(html.find('span',{"class":"css-1q7zgjd eclomwz0"}).text)
  area.append(html.find('span',{"class":"css-17o293g es62z2j18"}).text)
  developer.append(html.find('span',{"class":"css-e4snp0 es62z2j9"}).text)
  investment_type.append(html.find('div',{"class":"css-gkp38j es62z2j11"}).find('span').next_sibling)
  m2.append(html.find('span',{"class":"css-1q7zgjd eclomwz0"}).next_sibling.text)

pd.DataFrame(
    {'Name': name,
     'Price':price,
     'Pokoje':pokoje,
     'Area':area,
     'Developer':developer,
     'Investment Type':investment_type,
     'm2':m2
     }
)
