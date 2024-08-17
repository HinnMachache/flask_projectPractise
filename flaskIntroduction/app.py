from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'The Weeknd',
        'title': 'Out of Time',
        'content': 'First best post',
        'date_released': '12-02-2022'
    },
    {
        'author': 'Abel Makkonen',
        'title': 'Heartless',
        'content': 'Second best song',
        'date_released': '12-02-2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts, title='Home')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/makk')
def makk():
    return render_template("makk.html")


if __name__ == "__main__":
    app.run(debug=True)
    