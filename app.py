from flask import *
from database import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World test!'

@app.route('/create', methods=['GET', 'POST'])
def homepage():
	if request.method == 'GET':
		return render_template('form.html')
	else:
		name = request.form['name']
		age = request.form['age']
		subject = request.form['subject']

		save_to_database(name, age, subject)
		return render_template('response.html',
			n = name,
			a = age,
			s = subject)

if __name__ == '__main__':
    app.run(debug=True)