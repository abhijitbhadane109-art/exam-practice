from flask import Flask, render_template
app = Flask(__name__)
courses = [
"Python",
"Java",
"C Programming",
"Web Development",
"Data Science"
]
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/courses")
def courses_page():
    return render_template("courses.html", courses=courses)
app.run(debug=True)