import requests # take data from website, pip3
from bs4 import BeautifulSoup #bs4 larger folder with beautifulsoup & other things, reformats html code
from collections import defaultdict
import re
from ClinicalTrial import ClinicalTrial
from TrialsList import TrialsList

def strong_format(a_list):
    for i in range(len(a_list)): # loop by index
        a_list[i] = a_list[i].text
    return a_list

def convert_m_to_y(a_list):
    new_list = list()# new list and make changes to new list, 2 yrs 6 months shouldn't come up
    
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

def convert_y_to_m(a_list):
    new_list = list()
    for i in range(len(a_list)):
        age = ""
        months = 0
        
        index = a_list[i].find("year")
        num_y = int(a_list[i][:index-1])
        while True:
            if num_y > 0:
                months+=12
                num_y-=1
            else: 
                break
        
        if months > 1:
            age = str(months) + " months"
        elif months == 1:
            age = "1 month"
        new_list.append(age)
    return new_list

def dash_case(age): # the dash case, find dash and get 2 numbers on either side of dash
    split_age = age.split("-")
    months = list()
    display_age = ""
    for i in range(len(split_age)):
        months.append(int(split_age[i]) * 12)
        display_age = display_age + split_age[i] + " years "
        if i == 0:
            display_age+="to "
    return display_age, months

def up_to_case(age): # check years vs months, then convert to years & months
    # doesn't pop up
    display_age = "0 years to "
    age_list = [0]
    years = re.search("[0-9]+.year", age)
    months = re.search("[0-9]+.month", age)
    if years:
        display_age = display_age + years.string
        index_year = age.find("year")
        index_upto = age.find("up to")
        num_y = int(years.string[index_upto + 5:index_year-1])
        age_list.append(num_y * 12)
    if months:
        index = age.find("month")
        index_upto = age.find("up to")
        num_m = int(months.string[index_upto + 5:index-1])
        age_list.append(num_m)
        # num_m/=12
        if num_m == 1:
            display_age = display_age + str(num_m) + " month"
        else: 
            display_age = display_age + str(num_m) + " months"
        # display_age = display_age + str(num_m)
    return display_age, age_list

def and_up_case(age):
    display_age = ""
    age_list = []
    index_andup = age.find("and up")
    years = re.search("[0-9]+.year", age)
    months = re.search("[0-9]+.month", age)
    if years:
        display_age = display_age + years.string
        index_year = age.find("year")
        num_y = int(years.string[:index_year])
        age_list.append(num_y * 12)
    if months:
        index_month = age.find("month")
        num_m = int(months.string[:index_month])
        age_list.append(num_m)
        # num_m/=12
        if num_m == 1:
            display_age = display_age + str(num_m) + " month"
        else: 
            display_age = display_age + str(num_m) + " months"
    age_list.append(1000*12)
    return display_age, age_list
    # up to 100 years

def same_case(age):
    display_age = ""
    age_list = []
    # index_andup = age.find("and up")
    years = re.search("[0-9]+.year", age)
    months = re.search("[0-9]+.month", age)
    if years:
        display_age = display_age + years.string
        index_year = age.find("year")
        num_y = int(years.string[:index_year])
        age_list.append(num_y * 12)
        index_year2 = age.find("year", index_year + 1, len(age))
        num_y2 = 3
        if num_y == 1:
            num_y2 = int(years.string[index_year + 8:index_year2])
        else:
            num_y2 = int(years.string[index_year + 9:index_year2])
        age_list.append(num_y2 * 12)
    if months:
        display_age = display_age + months.string
        index_month = age.find("month")
        num_m = int(months.string[:index_month])
        age_list.append(num_m)
        index_month2 = age.find("month", index_month + 1, len(age))
        num_m2 = 3
        if num_m == 1:
            num_m2 = int(months.string[index_month + 9:index_month2])
        else:
            num_m2 = int(months.string[index_month + 10:index_month2])
        age_list.append(num_m2)
    return display_age, age_list

def months_years_case(age):
    display_age = ""
    age_list = []
    index_to = age.find("to")
    # index_andup = age.find("and up")
    years = re.search("[0-9]+.year", age)
    months = re.search("[0-9]+.month", age)
    # months
    display_age = display_age + months.string
    index_month = age.find("month")
    num_m = int(months.string[:index_month])
    age_list.append(num_m)
    # years
    # display_age = display_age + " to " + years.string
    index_year = age.find("year")
    num_y = int(years.string[index_to + 3:index_year])
    age_list.append(num_y * 12)
    return display_age, age_list

def get_info1(strong):
    age_display = ""
    age = [0,12000]
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
        age_display = person_type[start_index + 5:]
        matches_y = re.findall("[0-9]+.year", age)
        matches_m = re.findall("[0-9]+.month", age)
        # print(matches_y, matches_m)
        # print(matches_m)
        if len(matches_m) == 0 and len(matches_y) == 0: # case 1: no months or years
            age_display, age = dash_case(age)
            # return dash_case(age)
        elif (len(matches_m) == 1 and len(matches_y) == 0) or (len(matches_m) == 0 and len(matches_y) == 1): # case 2: __ and up or up to __
            if age.find("up to") != -1:
                age_display, age = up_to_case(age)
                # return up_to_case(age)
            
            else:
                age_display, age = and_up_case(age)
                # return and_up_case(age)
        elif len(matches_m) == 1 and len(matches_y) == 1: # months to years
            age_display, age = months_years_case(age)
        else:
            age_display, age = same_case(age)
            # return same_case(age)
        
        # if its ___ months to ___ months
    # print(focus)
    # print(strong)
    return person, focus, age_display, age # unchangeable tuple, immutable       

get_info1(["healthy people", "ages 4 years to 9 years"])


def fetch_data(): # code to scrape data
    # Get latest Trials
    url = 'https://ucla.clinicaltrials.researcherprofiles.org/browse/healthy'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib') # tells beautifulsoup that it's in html5, look for tags/classes



    trials = TrialsList()

    info = soup.find('ul', attrs = {'class':'list-unstyled'}) # first one it finds
    info2 = info.find_all('div', attrs = {'class': 'card-body'}) # puts into list

    for i in info2:
        a = i.find('a', attrs = {'class': 'stretched-link'})

        name = a.text
        link = a.get('href')
        strong = i.find_all('strong') # list
        strong = strong_format(strong)

        split_person = strong[-1].split()

        person = split_person[1]
        focus = strong[0:(len(strong)-1)]

        person, focus, age_display, age = get_info1(strong)

        ct = ClinicalTrial(name,person,focus,age)
        trials.append(ct)

    return trials
