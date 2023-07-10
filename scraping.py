import requests # take data from website, pip3
from bs4 import BeautifulSoup #bs4 larger folder with beautifulsoup & other things, reformats html code
from collections import defaultdict
import re

def strong_format(a_list):
    for i in range(len(a_list)): # loop by index
        a_list[i] = a_list[i].text
    return a_list

def convert_m_to_y(a_list):
    new_list = list() # new list and make changes to new list, 2 yrs 6 months shouldn't come up
    
    for i in range(len(a_list)):
        age = ""
        years = 0
        index = a_list[i].find("month")
        num_m = int(a_list[i][:index-1])
        
        while True:
            # print(num)
            if num_m >= 12:
                years+=1
                num_m-=12
            else:
                break

        if years > 1:
            age = str(years) + " years "
        elif years == 1:
            age = "1 year "
        
        if num_m > 1:
            age = age + str(num_m) + " months"
        elif num_m == 1:
            age = age + " 1 month"
        # print(age)
        new_list.append(age)
    return new_list



def get_info(strong):
    age = "ALL"
    person_type = strong[-1]
    split_person = person_type.split()
    # print(split_person)
    person = split_person[1] # to return
    if person == "people":
        person = "ALL"
    focus = strong[0:(len(strong)-1)] # to return
    if "ages" in person_type:
        start_index = person_type.find("ages")
        age = person_type[start_index + 5:]
        matches = re.findall("[0-9]+.month", age)
        years = convert_m_to_y(matches)
        for i in range(len(matches)):
            print(age)
            index = age.find(matches[i])
            print(matches[i])
            print(index)
            age = years[i] + age[index + len(matches[i]):]
        
    # print(focus)
    # print(strong)
    return person, focus, age # unchangeable tuple, immutable    

def fetch_data(): # code to scrape data
    data = defaultdict(list) # dictionary w/ values that are lists
    info = soup.find('ul', attrs = {'class':'list-unstyled'}) # first one it finds
    # info = info.prettify()
    # print(info)
    info2 = info.find_all('div', attrs = {'class': 'card-body'}) # puts into list
    # print(info2[0])
    # newset = set()
    for i in info2:
        a = i.find('a', attrs = {'class': 'stretched-link'})
        # print(name.text) # part of beautifulsoup
        name = a.text
        link = a.get('href')
        strong = i.find_all('strong') # list
        strong = strong_format(strong)
        # print(strong[-1]) # last item in list
        split_person = strong[-1].split()
        # print(split_person)
        person = split_person[1]
        focus = strong[0:(len(strong)-1)]
        #  print(focus)
        # print(strong)
        # newset.add(split_person[1])
        person, focus, age = get_info(strong)
        print(person, focus, age)
        # print(get_info(strong))
    # print(newset)



url = 'https://ucla.clinicaltrials.researcherprofiles.org/browse/healthy'
r = requests.get(url)
# print(r.content) # r.content gets the data from the url
soup = BeautifulSoup(r.content, 'html5lib') # tells beautifulsoup that it's in html5, look for tags/classes
# print(soup)
fetch_data()