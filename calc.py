def calculate(scorelist):	
	# named the value of each question 'score' for now
    results_a = scorelist('q1') * (scorelist('q2') / 30.5) * scorelist('q3')
    results_b = scorelist('q4') ? (scorelist('q5') * scorelist('q6')) : scorelist('q7') * 0.25 # weight for answer 2.1.2
    results_c = (scorelist('q8') * scorelist('q9') * scorelist('q10') * scorelist('q11') + scorelist('q12') * scorelist('q13')) / 2 # normalization factor
    results_d = (scorelist('q14') + scorelist('q15')) / 2 # normalization factor
    results_e = ((scorelist('q16') * scorelist('q17') * scorelist('q18') * scorelist('q19')) + scorelist('q20') +  scorelist('q21') + scorelist('q22') + scorelist('q23') + (scorelist('q24') * scorelist('q25') * scorelist('q26')) + (scorelist('q27') * scorelist('q28'))) / 7 # normalization factor
	
	weight_a = 30
	weight_b = 30
	weight_c = 30
	weight_d = 20
	weight_e = 20
	
	return results = ( results_a > 0.6 ) ? results_a : ( result_a * weight_a + result_b * weight_b + result_c * weight_c + result_d * weight_d + result_e * weight_e )
