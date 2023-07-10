from flask import Flask, request, jsonify
import json
import scrapingtest
app = Flask(__name__)

@app.route("/get_age", methods = ["GET", "POST"])

def sorted_age():
    all_dict = scrapingtest.fetch_data()
    print(all_dict["age"])
    order = sorted(list(range(len(all_dict["age"]))), key=lambda i: all_dict["age"][i][0])
    print('\n\n\n')
    print(order)
    print('\n\n\n')
    print(all_dict.keys())

    # 
    # return order
    return "done"
# ghost printing the ages

@app.route("/321")

def new_func():
    return "hello"

@app.route("/world")

def world_func():
    return "world"

# another file can't run this piece
if __name__ == "__main__":
    app.run(host='0.0.0.0')