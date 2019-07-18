from flask import Flask, render_template, request, url_for, redirect, request, session, flash
from database import *
app = Flask(__name__)
app.secret_key = "jrg;quoeiohqei833y2y8h"

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/profile")
def profile():
    user=auth_user("shelly",1234)
    stories=story_by_name(user.username)
    return render_template("profile.html", user=user, stories=stories)

@app.route("/aboutUs")
def aboutUs():
	return render_template("aboutUs.html")

@app.route("/stories")
def stories():
	stories=get_all_stories()
	return render_template("stories.html", stories=stories)

@app.route("/story/<int:id>")
def story(id):
	story=get_story_id(id)
	ids=get_all_id()
	n=id+1
	p=id-1
	if id==ids[-1]:
		n=1
	if id==1:
		p=ids[-1]

	return render_template("story.html", story=story, n=n, p=p)

@app.route("/events")
def events():
	events=get_all_events()
	return render_template("events.html", events=events)

@app.route("/event/<int:id>")
def event(id):
	event=get_event_id(id)
	return render_template("event.html", event=event)

@app.route("/submit")
def submit():
		return render_template ("submit.html")

@app.route("/store")
def store():
	products=get_all_products()
	return render_template("store.html", products=products)

@app.route("/product/<int:id>")
def product(id):
	product=get_product_id(id)
	more=get_more_product(id)
	more=more[0:3]
	return render_template("product.html", product=product, more=more)
	
if __name__ == '__main__':
    app.run(debug=True)
