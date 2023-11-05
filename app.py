from flask import Flask,request,render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "I-dont-know-what-this-is-for"

debug = DebugToolbarExtension(app)

@app.route("/")
def home():
    return render_template("home.html",stories=stories.values())

@app.route("/questions")
def questions():
    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts

    return render_template("questions.html",story_id=story_id,title=story.title,prompts=prompts)

@app.route("/story-generator")
def storygenerator():
    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)
    return render_template("story-generator.html", title = story.title,text = text)

