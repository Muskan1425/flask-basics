from flask import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('sum.html')

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

app.run(debug=True)