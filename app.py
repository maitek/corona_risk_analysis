from flask import Flask, render_template, request
import os
import yaml
app = Flask(__name__)


@app.route('/')
def root():
    # load questions
    with open("questions.yaml") as f:
        poll_data_array = yaml.load(f)

    return render_template('main.html', data=poll_data_array)
 
@app.route('/poll')
def poll():

    # parse results
    score_data = dict()
    with open("questions.yaml") as f:
        poll_data_array = yaml.load(f)
    
    for item in poll_data_array:
        name = item["name"]
        print(item)
        if item["type"] == "radio":
            score_data[name] = request.args.get(name)
    
    data = dict()
    data["results"] = score_data["q1"]
    return render_template('results.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)

