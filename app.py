from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
	#read values
	_value1 = request.form['value1']
	_value2 = request.form['value2']
	print("First value is'" + _value1 + "'")
	print("Second value is'" + _value2 + "'")
	return redirect('/')
	#check values
	#if _value1 and _value2:
	#	return json.dumps({'html':'<span>All fields received</span'})
	#else
	#	return json.dumps({'html':'<span>Required fields missing</span>'})

if __name__ == "__main__":
	app.run(debug=True)