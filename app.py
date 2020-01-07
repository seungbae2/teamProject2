from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#import scrape_mars
import requests
import os


app = Flask(__name__)
#app._static_folder = os.path.abspath("templates/static/")
#mongo = PyMongo(app, uri = 'mongodb://localhost:27017/mars_db')

@app.route("/")
def home():
	#mars_data = mongo.db.collection.find_one()

	return render_template("index.html")

# @app.route("/scrape")
# def scrape():

# 	nhl_data = scrape_mars.scrape()

# 	mongo.db.collection.update({}, nhl_data, upsert=True)

# 	return redirect("/")


if __name__ == "__main__":
	app.run(debug=True)