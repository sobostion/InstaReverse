from flask import Flask, render_template, request
from forms import ContactForm
from flask_wtf import Form
from wtforms import TextField

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def index():
        return "<h1>omg it's flask</h1>"

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()

   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
         return render_template('success.html')
   elif request.method == 'GET':
         return render_template('contact.html', form = form)

if __name__ == "__main__":
        app.run(debug=True)
