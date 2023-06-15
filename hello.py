from flask import Flask
# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return "Hello World!"
# run the application
app.run(debug=True)