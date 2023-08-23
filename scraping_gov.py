import requests # take data from website, pip3
from bs4 import BeautifulSoup #bs4 larger folder with beautifulsoup & other things, reformats html code

from collections import defaultdict
import re

from clinicaltrial import clinicaltrial
from trialslist import trialslist

def fetch_gov_data(): # code to scrape data

    # get latest trials
    url = 'https://clinicaltrials.gov/search?aggFilters=status:rec%20not&limit=100&page=1' # page 1 of 100
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup)

    trials = trialslist()
    # data = defaultdict(list) # dictionary w/ values that are lists
    # info = soup.find('div', attrs = {'class':'bg-white desktop:margin-top-4'}) # first one it finds
    # info = info.prettify()
    # print(info)
    # info2 = info.find_all('div', attrs = {'class': 'card-body'}) # puts into list
    # print(info2[0])
    # newset = set()

fetch_gov_data()
    