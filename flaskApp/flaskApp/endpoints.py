from flaskApp import app

from flask import render_template

@app.route("/")
def index():
    return render_template('publicTemplates/index.html')

@app.route("/about")
def about():
    return render_template('publicTemplates/about.html')

@app.route("/coolPic")
def getPic():
	return render_template('publicTemplates/cat.html')

@app.route("/jinja")
def jinja():
	name = "AJ"
	return render_template('publicTemplates/jinja.html',name=name)