from flask import Flask, request, jsonify
import json
import scrapingtest
import trialslist

app = Flask(__name__)

@app.route("/get_trials", methods = ["GET", "POST"])

def get_trials():
    all_trials = scrapingtest.fetch_data()
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
    age = request.form["age"] # get info from age in postman, not somewhere on the internet where others can access
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
    all_trials = scrapingtest.fetch_data() # trialslist of all data
    set_of_focuses = set()
    for i in all_trials.trials:
        for j in i.focus:
            set_of_focuses.add(j)
    print(set_of_focuses)
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
    
    # return "6"

# another file can't run this piece
if __name__ == "__main__":
    app.run(host='0.0.0.0')