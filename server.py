from flask import Flask, request, jsonify
import json
import scrapingtest
import trialslist
import database
from recommendation import get_recommendation


app = Flask(__name__)

@app.route("/get_trials", methods = ["GET", "POST"])
def get_trials():
    all_trials = scrapingtest.fetch_data()
    trials_list2 = database.get_data()
    all_trials.trials = all_trials.trials + trials_list2.trials
    
    return all_trials.get_json()
    # print(all_dict["age"])
    # order = sorted(list(range(len(all_dict["age"]))), key=lambda i: all_dict["age"][i][0])
    # print(order)
    # return order
    # to_print = list()
    # for i in order:
        # 3
    # return "done"

@app.route("/user_info_trials", methods = ["GET", "POST"]) 
def user_info_trials():
    # print("1234")
    age = request.form["age"] # get info from age in postman, not somewhere on the internet where others can access
    # print(age)
    if age == "z":
        age = None
    else:
        age = int(age) * 12
    gender = request.form["gender"]
    if gender == "z":
        gender = None
    focus = request.form["focus"]
    if focus == "z":
        focus = None
    sort_by = request.form["sort"]
    print(age, gender, focus, sort_by)
    all_trials = scrapingtest.fetch_data() # trialslist of all data
    trials_list2 = database.get_data()
    all_trials.trials = all_trials.trials + trials_list2.trials
    set_of_focuses = set()
    for i in all_trials.trials:
        for j in i.focus:
            set_of_focuses.add(j)
    # print(set_of_focuses)
    all_trials.trials = all_trials.filter(age = age, gender = gender, focus = focus)
    # a = age, b = gender, c = focus, z = none, n = name (alphabetical)
    if sort_by == "a":
        all_trials.sort_age()
    elif sort_by == "n":
        all_trials.sort_name()
    # elif sort_by == "b":
        # all_trials.sort_gender()
    # elif sort_by == "c":
        # all_trials.sort_focus()

    # for i in all_trials.trials:
        # print(i.get_age_range())
    # print(all_trials.trials)
    return all_trials.get_json()

@app.route("/get_focuses", methods = ["GET", "POST"])

def get_focuses():
    all_trials = scrapingtest.fetch_data()
    return all_trials.all_focuses()

@app.route('/test')
def hh():
    return "hello"
    # return "6"




@app.route('/recommendation', methods = ["GET", "POST"])
def recommendation():
    all_trials = scrapingtest.fetch_data()
    trials_list2 = database.get_data()
    all_trials.trials = all_trials.trials + trials_list2.trials

    age = request.form["age"] # get info from age in postman, not somewhere on the internet where others can access
    if age == "z":
        age = 30
    else:
        age = int(age)

    gender = request.form["gender"]
    if gender == "z":
        gender = 'all'

    ethnicity = request.form["ethnicity"]
    if ethnicity == "z":
        ethnicity = 'N/A'


    jsonBody = all_trials.get_json()
    recommendationsList = get_recommendation(all_trials, age, ethnicity, gender).tolist()
    # jsonBody['recommendations'] = recommendations

    trialRecommendations = trialslist.trialslist()

    for trial in all_trials.trials:
        if trial.name in recommendationsList:
            trialRecommendations.append(trial)

    print(age, gender, ethnicity)
    # trialRecommendations.print_trials_data()
    return trialRecommendations.get_json()



# [
#     "The Evaluation of PC14586 in Patients With Advanced Solid Tumors Harboring a p53 Y220C Mutation (PYNNACLE)", 
#     "Adaptation of the PCIP for Children Aged 6 to 11", 
#     "The Effect of Opioid-Free Anesthesia in TMJ Surgery", 
#     "A Study to Evaluate the Safety, Reactogenicity, and Effectiveness of mRNA-1273 Vaccine in Adolescents 12 to <18 Years Old to Prevent COVID-19", 
#     "Pilot Study for OCT Guided In Vivo Laser Capture Microdissection for Assessing the Prognosis of Barrett's Esophagus"
#     ]

# ["A Study of Daily Oral Orforglipron (LY3502970) Compared With Insulin Glargine in Participants With Type 2 Diabetes and Obesity or Overweight at Increased Cardiovascular Risk", 
#  "A Phase 1b/2 Study of BGB-11417in Monotherapy and in Various Combinations With Dexamethasone and Carfilzomib in Multiple Myeloma", 
#  "Protective Ventilation With High Versus Low PEEP During One-lung Ventilation for Thoracic Surgery", 
#  "A Study of Teclistamab in Combination With Daratumumab Subcutaneously (SC) (Tec-Dara) Versus Daratumumab SC, Pomalidomide, and Dexamethasone (DPd) or Daratumumab SC, Bortezomib, and Dexamethasone (DVd) in Participants With Relapsed or Refractory Multiple Myeloma", 
#  "Circuit-Based Approach to Suicide: Biomarkers, Predictors, and Novel Therapeutics"]



# another file can't run this piece
# if __name__ == "__main__":
app.run(host='0.0.0.0')
