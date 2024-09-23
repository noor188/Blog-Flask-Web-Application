from app import app, db
from flask import render_template, flash, redirect, url_for, request, abort
from app.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Post
import sqlalchemy as sa
from django.utils.http import url_has_allowed_host_and_scheme
from urllib.parse import urlsplit

@app.route('/')
@app.route('/index')
@login_required
def index():
    
    posts = [
    {
        'author': {'username':'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username':'Suzan'},
        'body': 'The Avengers movie was so cool!'
    }]
    return render_template('index.html', title='Home', posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():

        statment = sa.select(User).where( User.username== form.username.data)
        user = db.session.scalar(statment)
        if user is None or not (user.check_password(form.password.data)):
            flash("Username does not exist or invalid password")
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        flash("Login Requested for user {}, remember_me={}".format(form.username.data, form.remember_me.data))

        next = request.args.get('next')
        if not next or urlsplit(next).netloc != '':            
            next = url_for('index')
            
        #return redirect(next or url_for('index'))
        return redirect(next)
    return render_template("login.html", title='Sign In', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=["POST", "GET"])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)  

@app.route('/user/<username>')
@login_required
def user(username):
    '''

    Handles the user profile page

    '''
    statement_user  = sa.select(User).where(User.username == username)
    user            = db.first_or_404(statement_user)
    #statement_posts = sa.select(Post).where(Post.user_id == current_user.id )
    #posts = db.session.scalars(statement_posts)
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'},
    ]
    return render_template("user.html", user = user, posts = posts)

    

