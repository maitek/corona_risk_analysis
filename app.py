from flask import Flask, render_template
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
    # vote = request.args.get('field')
	
	# named the value of each question 'score' for now
    results_a = request.args.get('q1').get('score') * (request.args.get('q2').get('score') / 30.5) * request.args.get('q3').get('score')
    results_b = request.args.get('q4').get('score') ? (request.args.get('q5').get('score') * request.args.get('q6').get('score')) : request.args.get('q7').get('score') * 0.25 # weight for answer 2.1.2
    results_c = (request.args.get('q8').get('score') * request.args.get('q9').get('score') * request.args.get('q10').get('score') * request.args.get('q11').get('score') + request.args.get('q12').get('score') * request.args.get('q13').get('score')) / 2 # normalization factor
    results_d = (request.args.get('q14').get('score') + request.args.get('q15').get('score')) / 2 # normalization factor
    results_e = ((request.args.get('q16').get('score') * request.args.get('q17').get('score') * request.args.get('q18').get('score') * request.args.get('q19').get('score')) + request.args.get('q20').get('score') +  request.args.get('q21').get('score') + request.args.get('q22').get('score') + request.args.get('q23').get('score') + (request.args.get('q24').get('score') * request.args.get('q25').get('score') * request.args.get('q26').get('score')) + (request.args.get('q27').get('score') * request.args.get('q28').get('score'))) / 7 # normalization factor
	
	weight_a = 30
	weight_b = 30
	weight_c = 30
	weight_d = 20
	weight_e = 20
	
	results = ( results_a > 0.6 ) ? results_a : ( result_a * weight_a + result_b * weight_b + result_c * weight_c + result_d * weight_d + result_e * weight_e )
    return render_template('results.html', data=results)

if __name__ == "__main__":
    app.run(debug=True)

