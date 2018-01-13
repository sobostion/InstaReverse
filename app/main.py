from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import TextField

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
def front():
	return render_template('front.html')

if __name__ == "__main__":
        app.run(debug=True)
