from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_wtf import FlaskForm

# from app import routes
# from app import models

app = Flask(__name__)


# app.config["SQLALCHEMY_DATABASE_URI"]= 'postgres://mouse:gnusmas@localhost/cheese'
# app.config["SECRET_KEY"] = "secret key!"
# DEBUG = True


# db = SQLAlchemy(app)


# class MyForm(FlaskForm):
#     someData = TextField('Data:', validators=[validators.required()])

# class SomeData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     somedata = db.Column(db.String(200))

#     def __init__(self,somedata):
#         self.somedata = somedata


@app.route('/',methods=['GET', 'POST'])
def index():
    # form = MyForm()
    # all_data = SomeData.query.all()
    # if form.validate_on_submit():
    #     mydata = SomeData(somedata = form.someData.data)
    #     db.session.add(mydata)
    #     db.session.commit()
    #     return redirect(url_for('index'))


    # return render_template('index.html', title='Home', form=form, all_data = all_data)
    return render_template('index2.html')


