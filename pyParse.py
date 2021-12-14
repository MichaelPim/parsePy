import requests
from bs4 import BeautifulSoup
import csv


rs = requests.get('https://www.bestchange.ru/')
root = BeautifulSoup(rs.content, 'html.parser')



for tr in root.select('#content_table > tbody > tr'):

    name =  [tr.select_one('td.bj .pc .ca').get_text(strip=True)]
    reserve = [tr.select_one('td.arp').get_text(strip=True)]
    reviews = [tr.select_one('td.rw').get_text(strip=True)]



    [give_el, get_el] = tr.select('td.bi')
    give = [give_el.select_one('.fs').get_text(strip=True)]
    get = [get_el.get_text(strip=True)]

    
    stats_dictionary = zip(name,give,get,reserve,reviews)


    with open('data10.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(stats_dictionary)












