from flask import *
import numpy as np
app = Flask (__name__)

@app.route("/")
def home():
    return render_template("sum.html")

@app.route('/add',methods = ['POST','GET'])
def result(sum):
    if request.method == 'POST': 
      a=request.form['Entered number1']
      b=request.form['Entered number2']
      x=int(a)
      y=int(b)
      sum = x+y
    return 'sum of given number: %s' %sum
       
app.run(debug=True)