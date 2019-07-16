from flask import Flask, render_template, request, url_for, redirect, request, session, flash
from database import auth_user, add_user, add_story, story_by_name, get_all_stories, get_story_id, get_all_events, get_event_id
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
	return render_template("story.html", story=story)

@app.route("/events")
def events():
	events=get_all_events()
	return render_template("events.html", events=events)

@app.route("/event/<int:id>")
def event(id):
	event=get_event_id(id)
	return render_template("event.html", event=event)

@app.route("/submit", methods=['GET', 'POST'])
def submit():
	if request.method == 'GET':
		return render_template ("submit.html")
	else:
		title= request.form['title']
		story= request.form['story']
		name="gorge"
		add_story(name,title,story)
		return redirect(url_for("/"))





if __name__ == '__main__':
    app.run(debug=True)
