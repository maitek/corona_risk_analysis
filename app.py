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

    data = dict()
    data["results"] = request.args.get('q1')
    return render_template('results.html', data=data)
    
if __name__ == "__main__":
    app.run(debug=True)

