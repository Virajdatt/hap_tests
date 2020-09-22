from flask import Flask, render_template, jsonify, request
from textblob import TextBlob


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def TB():
  if request.method == 'POST':
  	n = TextBlob(request.form.get('sentence')).sentiment.polarity
  	if n > 0.0:
  		return "<h2>POSITIVE REVIEW</h2>"
  	elif n == 0.0:
  		return "<h2>NEUTRAL</h2>"
  	else:
  		return "<h2>NEGATIVE REVIEW</h2>"
  


  return '''<textarea rows="4" cols="50">
         Please enter the sentence for which you want the sentiment for.
         </textarea>
         <form method="POST">
                  Sentence: <input type="text" name="sentence" size="15"><br>
                 
                  <input type="submit" value="Submit"><br>
              </form>
         '''

    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5000) 