from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import date, time, datetime
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'de'
babel = Babel(app)

def get_locale():
    # return 'de'
    return request.accept_languages.best_match(app.config['de', 'en', 'se'])


@app.route("/")
def index():
    anthony = gettext('Mr')

    us_num = numbers.format_decimal(12345, locale='en_US')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    de_num = numbers.format_decimal(12345, locale='de_DE')
    ke_num = numbers.format_decimal(12345, locale='en_KE')

    current_date = date.today()

    us_date = dates.format_date(current_date, locale='en_US')
    se_date = dates.format_date(current_date, locale='sv_SE')
    de_date = dates.format_date(current_date, locale='de_DE')
    ke_date = dates.format_date(current_date, locale='en_KE')


    results = {
        "us_num" : us_num,
        "se_num" : se_num,
        "de_num" : de_num,
        "ke_num" : ke_num,
        "us_date" : us_date,
        "se_date" : se_date,
        "de_date" : de_date,
        "ke_date" : ke_date

    }
    return render_template("index.html", results=results, anthony=anthony)



if (__name__) == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)

