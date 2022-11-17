from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/animals')
def animals():
    return render_template('animals.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/walks')
def walks():
    return render_template('walks.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


# @app.route('/login')
# def login_():
#     return render_template('login.html')
