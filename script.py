import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import string
from urllib.request import urlopen
import pandas as pd
import requests
pd.options.mode.chained_assignment = None 

url = 'https://www.editus.lu/fr/resultats/medecine-professions-medicale-paramedicale/medecin-dentiste-1071r'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0'}
response_1 = requests.get(url,headers=headers)
soup_1 = BeautifulSoup(response_1.content, 'html.parser')

htmls = soup_1.findAll('h2',{"class":"name"})
links=[]
for html in htmls:
    links.append(html.find('a').get('href'))
response_2 = requests.get(links[0],headers=headers)
soup_2 = BeautifulSoup(response_2.content, 'html.parser')

name = []
company_name=[]
position=[]
company_email=[]
person_email=[]
telephone=[]
website=[]
postal_address=[]

for link in links:
    response_2 = requests.get(link,headers=headers)
    soup_2 = BeautifulSoup(response_2.content, 'html.parser')
    name.append(soup_2.find('h3',{"class":"name"}).text.strip()) #name
    company_name.append(soup_2.find('h1',{"class":"name"}).text.strip()) #company_name
    position.append(soup_2.find('span',{"class":"activity"}).text.strip()) #position
    try:
        company_email.append(soup_2.find('a',{"data-key":"fi-act-email-contact"}).get('href')[7:]) #email
    except AttributeError:
        company_email.append('No email found')
    try:
        telephone.append(soup_2.find('a',{"data-key":"fi-act-call-contact"}).get('href')[4:]) #phone
    except AttributeError:
        telephone.append('No telephone found')
    website.append(link) #website
    postal_address.append(soup_2.find('span',{"class":"address"}).text.strip().replace("\n",', ')) #address

pd.DataFrame(
    {
        "Name":name,
        "Company Name":company_name,
        "Position":position,
        "Email":company_email,
        "Telephone":telephone,
        "Website":website,
        "Postal Address":postal_address
    }
)
