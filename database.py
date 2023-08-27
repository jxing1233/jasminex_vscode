import pandas as pd
from clinicaltrial import clinicaltrial
from trialslist import trialslist

def get_data():
    df = pd.read_csv('CA_MA_studies.csv')

    # print(df.head()) # prints first 5

    columns = list(df.columns.values)
    # print(columns)
    del(columns[0])
    # df = df.drop(df['ID'], axis = 1)
    # print(df)
    df = df[['name','study','gender','age','start_month','location','ethnicity']]

    df = df.drop(df[df['location'] == 'UCLA'].index)
    # print(df['location'])

    trials_list = trialslist()
    for i in df.index: # i is each number of the rows
        found = False
        # print(i)
        if len(trials_list.trials) == 0:
            trial = clinicaltrial(df['name'][i], df['gender'][i], {df['study'][i]}, df['age'][i], 'N/A', df['location'][i], df['start_month'][i], {df['ethnicity'][i]})
            trials_list.append(trial)
            continue # goes onto the next i value, else also works
        # for j in trials_list.trials:
        if trials_list.trials[-1].name == df['name'][i]:
            trials_list.trials[-1].focus.add(df['study'][i])
            trials_list.trials[-1].ethnicity.add(df['ethnicity'][i])
            # print(j.name)
            found = True
        if found == False:
            trial = clinicaltrial(df['name'][i], df['gender'][i], {df['study'][i]}, df['age'][i], 'N/A', df['location'][i], df['start_month'][i], {df['ethnicity'][i]})
            trials_list.append(trial)
            # print(trials_list.trials)
        # break

    for i in trials_list.trials:
        i.focus = list(i.focus)
        i.ethnicity = list(i.ethnicity)
        
    return trials_list
        
    

