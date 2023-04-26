from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from datetime import date
from wtforms.fields.html5 import DateField
from wtforms.validators import url, DataRequired, Email, EqualTo, Length
import json

class StockForm(FlaskForm):
    """Generate your Graph."""

    x = open('flask_wtforms_tutorial/nyse-listed_json.json')
    jdata = json.load(x)
    x.close()
    allSymbols = []
    apiKey = 'TBV7EY1WFDG25BLY'

    for i in range(len(jdata)):
        allSymbols.append((jdata[i]["ACT Symbol"],jdata[i]["ACT Symbol"]))

    symbol = SelectField("Choose Stock Symbol",[DataRequired()],
        choices=allSymbols
    )


    chart_type = SelectField("Choose A Chart Type", [DataRequired()],
        choices=[
            ("1", "1. Bar"),
            ("2", "2. Line"),

        ],
    )

    time_series = SelectField("Choose A Time Series", [DataRequired()],
        choices=[
            ("1", "1. Intraday"),
            ("2", "2. Daily"),
            ("3", "2. Weekly"),
            ("4", "4. Monthly"),
        ],
    )

    start_date = DateField("Enter Start Date")
    end_date = DateField("Enter End Date")
    submit = SubmitField("Submit")

