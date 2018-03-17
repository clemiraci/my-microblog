from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/') # these app route commands pass the url correspoding to the page
@app.route('/index')
def index():
    user = {'username': 'Clemente'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },

        {
            'author': {'username': 'JC'},
            'body': 'This microblog looks like twitter'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)