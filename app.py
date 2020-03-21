from flask import Flask, render_template
import os
app = Flask(__name__)
 
poll_data_array = [
  {
   'question' : 'Did you travel with public transport the last 14 days?',
   'fields'   : ['Yes', 'No'],
   'type'     : 'radio'
  },
  {
   'question' : 'How many people did you have close contact with (less than 2 meters)?',
   'fields'   : ['None', '1-10', '10-100', 'More than 100'],
   'type'     : 'radio'

  },
  {
   'question' : 'Do you have any of these symptoms? ',
   'fields'   : ['Fever', 'Cough', 'Shortness of breath'],
   'type'     : 'checkbox'
  },


]
   #'question' : 'How many people did you have close contact with (Less than 2 meters)?',
      #'fields'   : ['None', '1-10', '10-100', 'More than 100']

@app.route('/')
def root():
    return render_template('main.html', data=poll_data_array)
 
if __name__ == "__main__":
    app.run(debug=True)
