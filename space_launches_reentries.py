import requests
import pandas as pd
from time import gmtime, strftime
from csv import writer
from bs4 import BeautifulSoup
from csv import writer
import re

#########################################################################################################
#LTT Backpack Code below
#########################################################################################################

datetime = strftime("%Y-%m-%d %H:%M:%S")

URL = "https://www.faa.gov/data_research/commercial_space_data/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "lxml")

type = []
date = []
vehicle = []
company = []
site = []

for caption in soup.find_all('caption'):
    for x in ('Most Recent Licensed Launches','Most Recent Licensed Reentries','Most Recent Permitted Launches'):
        if caption.get_text() == x:
            type.append(x)
            type.append(x)
            type.append(x)
            temp = caption.find_parent('table', {'class': 'responsive'})

            for i in ('Date','Vehicle','Company','Site'):
                for n in temp.find_all("td", {"data-heading": i}):
                    # print(n.get_text().strip())

                    if   i == 'Date':
                        date.append(n.get_text().strip())
                    elif i == 'Vehicle':
                        vehicle.append(n.get_text().strip())
                    elif i == 'Company':
                        company.append(n.get_text().strip())
                    elif i == 'Site':
                        site.append(n.get_text().strip())

data = [type, date, vehicle, company, site]

df = pd.DataFrame(list(zip(type, date, vehicle, company, site)), columns=['type','date','vehicle','company','site'])
    
df['query_date'] = pd.Timestamp.today().strftime('%Y-%m-%d')

df.to_csv('space_launches_reentries.csv', mode='a', index=False, header=False)