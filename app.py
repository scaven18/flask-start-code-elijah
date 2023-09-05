# This is your library
from flask import Flask, render_template

# This initiates the flask app
app = Flask(__name__)

# We are telling flask where to go for home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about.html')

# Runs your flask app
if (__name__ == "__main__"):
    app.run(debug=True)
