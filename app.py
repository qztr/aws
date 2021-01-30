from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# from app import routes
# from app import models

app = Flask(__name__)


SQLALCHEMY_DATABASE_URI = 'postgres://mouse:gnusmas@localhost/cheese'
SECRET_KEY = "secret key!"
DEBUG = True


db = SQLAlchemy(app)


class MyForm(Form):
    someData = TextField('Name:', validators=[validators.required()])

class SomeData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    somedata = db.Column(db.String(200))

    def __init__(self,status):
        self.status = status


@app.route('/')
@app.route('/index')
def index():
    form = MyForm()
    if form.validate_on_submit():
        mydata = SomeData(somedata = form.someData.data)
        db.session.add(mydata)
        db.session.commit()

        all_data = SomeData.query.all()

    return render_template('index.html', title='Home', form=form, all_data = all_data)

