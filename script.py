from selenium import webdriver    # to  control the chrome browser
import time
from bs4 import BeautifulSoup     # to parse the page source
import pandas as pd                # to create csv file of scraped user details
from selenium.webdriver.chrome.options import Options
import re
import json

url_data = pd.read_csv('/Users/raihanafiandi/Documents/Upwork/A/SN URLs (external for scraping) - Sheet1.csv',header=None) # extract all the urls provided
url_data.values.tolist()
url_datas = []
for url in url_data.values.tolist():
    url_datas.append(url[0])
    
options = Options()
options.add_argument("user-data-dir=/Users/raihanafiandi/Library/Application Support/Google/Chrome/Default")
bro = webdriver.Chrome(chrome_options=options)    # creating chrome instance
record=[]
                        
for url in url_datas[:5]: #scrape the first 5 urls
    bro.get((url))             
    bro.implicitly_wait(20)                         # wait until the page load fully
    time.sleep(3)
    ss=bro.page_source                              # getting page source from selenium
    soup=BeautifulSoup(ss,'html.parser')            # parsing the page source with a html parser of Beautiful Soup
    time.sleep(1)
    try:
        names=soup.find("span",{"class":"profile-topcard-person-entity__name t-24 t-black t-bold"})
        name=names.text.strip()
    except:
        name="None"
    try:
        company_list = []
        companies = soup.findAll("a",{"class":"ember-view inverse-link-on-a-light-background font-weight-400"})
        for company in companies:
            company_list.append(company.text.strip())
        dict_company = {}
        for i,company in enumerate(company_list,1):
            dict_company[f'Company_{i}'] = company
    except:
        company='None'

    try:
        position_list = []
        positions = soup.findAll("dt",{"class":"profile-position__title t-16 t-16--open t-black t-bold"})
        for position in positions:
            position_list.append(position.text.strip())
        dict_position = {}
        for i,position in enumerate(position_list,1):
            dict_position[f'Position_{i}'] = position
    except:
        position='None'
        
    contacts=soup.findAll("a",{"class":"profile-topcard__contact-info-item-link inverse-link-on-a-light-background t-14"})
    try:
        website=contacts[0].get("href")
    except:
        website='None'
    try:
        twitter=contacts[1].get("href")
    except:
       twitter='None'
    
    output_dict = {'Name': name} | dict_company | dict_position | {'Website':website} | {'Twitter': twitter} | {'Navigator_Link': url}
    record.append(output_dict)
    
sample = json.dumps(record)
text_file = open("Output.txt", "w")
text_file.write(output)
text_file.close()
