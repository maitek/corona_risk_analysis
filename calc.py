def calculate(scorelist):	
    # named the value of each question 'score' for now
    results_a = scorelist.get('q1') * (scorelist.get('q2') / 30.5) * scorelist.get('q3')
    results_b = scorelist.get('q4') if (scorelist.get('q5') * scorelist.get('q6')) else scorelist.get('q7') * 0.25 # weight for answer 2.1.2
    results_c = (scorelist.get('q8') * scorelist.get('q9') * scorelist.get('q10') * scorelist.get('q11') + scorelist.get('q12') * scorelist.get('q13')) / 2 # normalization factor
    results_d = (scorelist.get('q14') + scorelist.get('q15')) / 2 # normalization factor
    results_e = ((scorelist.get('q16') * scorelist.get('q17') * scorelist.get('q18') * scorelist.get('q19')) + scorelist.get('q20') +  scorelist.get('q21') + scorelist.get('q22') + scorelist.get('q23') + (scorelist.get('q24') * scorelist.get('q25') * scorelist.get('q26')) + (scorelist.get('q27') * scorelist.get('q28'))) / 7 # normalization factor
	
    weight_a = 30
    weight_b = 30
    weight_c = 30
    weight_d = 20
    weight_e = 20

    return results = (results_a * 100) if ( results_a > 0.6 ) else ( results_a * weight_a + results_b * weight_b + results_c * weight_c + results_d * weight_d + results_e * weight_e )
