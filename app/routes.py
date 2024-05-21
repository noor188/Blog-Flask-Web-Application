from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Noor'}
    posts = [
    {
        'author': {'username':'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username':'Suzan'},
        'body': 'The Avengers movie was so cool!'
    }]
    return render_template('index.html', title='Home', user=user, posts=posts)

