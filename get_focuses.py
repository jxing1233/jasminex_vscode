import pandas as pd

df = pd.read_csv('CA_MA_studies.csv')

# print(df.head()) # prints first 5

columns = list(df.columns.values)
        # print(columns)
del(columns[0])
        # df = df.drop(df['ID'], axis = 1)
        # print(df)
df = df[['name','study','gender','age','start_month','location','ethnicity']]

set_focus = set()
for i in df.index:
    set_focus.add(df['study'][i])

print(set_focus) # create a page on the server that can allow to see everything? in json format?

import scrapingtest
import trialslist
all_trials = scrapingtest.fetch_data()