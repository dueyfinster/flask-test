from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask(__name__)
from .models import *
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    user = User(request.form['username'], request.form['message'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('message', username=user.username))

@app.route('/message/<username>')
def message(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('message.html', username=user.username,
                                           message=user.message)


