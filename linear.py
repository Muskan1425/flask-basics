import numpy as np
from sklearn.linear_model import LinearRegression
from flask import *

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route('/add',methods = ['POST','GET'])
def linear():
  if request.method == 'POST':
    a=request.form['Enter number']
    b= int(a)
    X = np.array([1,2,3,4,5]).reshape(-1,1)
    y = [2,4,6,8,10]
    reg = LinearRegression().fit(X, y)
    output = reg.predict(np.array([b]).reshape(-1,1))
    return "Predict value is %s" %output


app.run(debug=True)