from flask import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('frontend.html')

@app.route('/add',methods = ['POST'])
def add():
  if request.method == 'POST':
    first_nu = request.form['first number']
    second_nu =   request.form['second number']

  
  sum = int(first_nu) + int(second_nu)
  
  return render_template("frontend.html")%sum


app.run(debug = True)
