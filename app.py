import os
from flask import Flask, render_template, request, json, redirect

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
	#read values
	_value1 = request.form['value1']
	_value2 = request.form['value2']
	#print("First value is'" + _value1 + "'")
	#print("Second value is'" + _value2 + "'")
	if _value1[::-1] == _value2:
		return render_template('index.html', result = 'Yes, indeed it is.')
	else:
		return render_template('index.html', result = 'No, it is not.')
	#return redirect('/')
	
	#check values / not gonna use javascript afterall
	#if _value1 and _value2:
	#	return json.dumps({'html':'<span>All fields received</span'})
	#else:
	#	return json.dumps({'html':'<span>Required fields missing</span>'})

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)