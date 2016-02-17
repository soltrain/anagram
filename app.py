import os
from flask import Flask, render_template, request, json, redirect

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

def calcAnagram(var1, var2):
	x = 0
	i = 0
	match = True 
	var1 = var1.lower()
	var1 = sorted(var1)
	var2 = var2.lower()
	var2 = sorted(var2)
	#print 'sorted var1:', var1
	#print 'sorted var2:', var2

	if len(var1) == len(var2):
		for x in var1:
			if var1[i] == var2[i]: 
				i = i + 1
			else:
				match = False
				break
	else:
		match = False

	if match == False:
		return 0
	else:
		return 1

@app.route('/process', methods = ['POST'])
def process():
	#read values
	value1 = request.form['value1']
	value2 = request.form['value2']
	
	#print("First value is'" + value1 + "'")
	#print("Second value is'" + value2 + "'")
	#print(calcAnagram(value1,value2))
	
	if calcAnagram(value1,value2) == 0:
		return render_template('index.html', result = 'No, no anagram here.')
	else:
		return render_template('index.html', result = 'Yes, we have an anagram.')
	
	
if __name__ == "__main__":
	#need this for heroku 
	port = int(os.environ.get("PORT", 5000))
	#app.debug = True
	app.run(host='0.0.0.0', port=port)