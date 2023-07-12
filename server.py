from flask import Flask, request, jsonify
import json
import scrapingtest

from ClinicalTrial import ClinicalTrial
from TrialsList import TrialsList

app = Flask(__name__)

@app.route("/get_trials", methods = ["GET", "POST"])
def get_trials():
    all_trials = scrapingtest.fetch_data()
    return all_trials.get_json()


@app.route("/321")

def new_func():
    return "hello"

@app.route("/world")

def world_func():
    return "world"

# another file can't run this piece
if __name__ == "__main__":
    app.run(host='0.0.0.0')