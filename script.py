import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import string
from urllib.request import urlopen
import pandas as pd
import openpyxl
pd.options.mode.chained_assignment = None 

url = 'https://epss.ae/epss-members/'
soup = BeautifulSoup(urlopen(url), 'html.parser')

name=[]
city=[]
state=[]
email=[]
phone=[]
id=[]
member_since=[]

for i in soup.findAll('div',{"class":"box-right col-md-10"}):
    name.append(i.find('h3').text)
    city.append(i.find('span',{"class":"ehome_speaker_title"}).text)
    state.append(i.find('span',{"class":"ehome_speaker_country"}).text)
    bio=(i.find('p',{"class":"ehome_speaker_bio"}).text)
    try:
        email.append(re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', bio).group(0)) # regex to find email
    except AttributeError:
        email.append('no email found')
    try:
        phone.append(re.search(r'\b971\d{8,9}\b', bio.replace('-','').replace(' ','').replace(')','')).group(0)) #regex to find UAE phone number (starting with 971)
    except AttributeError:
        phone.append('no phone found')
    try:
        id.append(re.search('\d{2}-\d{3,4}', bio).group(0)) #regex to find id (starting with number with 2 digits following with - and ended with 3 or 4 digits)
    except AttributeError:
        id.append('no id found')
    try:
        member_since.append(re.search('\d{1,2}/\d{1,2}/\d{2,4}', bio).group(0)) #regex to find date
    except AttributeError:
        member_since.append('no data found')

pd.DataFrame(
    {"Name":name,
    "City":city,
    "State":state,
    "Email":email,
    "Phone":phone,
    "id":id,
    "Member since":member_since
    }
)
