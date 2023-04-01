from flask import Flask, render_template, redirect, session, request
from functools import wraps
import pymongo
from mic import list

app = Flask(__name__)
app.secret_key = b'\xf6\x90_\x7f~x\xe2{Q\x13a4(\xff{k'

# Database
client = pymongo.MongoClient('mongodb+srv://tatkariprem2002:ToOhHiPd7lYn5hFj@simplyfreshdb.twmkedc.mongodb.net/?retryWrites=true&w=majority')
db = client.vts

# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

# Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/main/')
def main():
    return render_template('main.html' , list=list)


