from flask import Flask, request, jsonify
import json
import scrapingtest



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

@app.route("/321")

def new_func():
    return "hello"

@app.route("/world")

def world_func():
    return "world"

# another file can't run this piece
if __name__ == "__main__":
    app.run(host='0.0.0.0')