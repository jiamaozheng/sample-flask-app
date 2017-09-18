#!/usr/bin/env

from flask import Flask, render_template, flash, request, redirect, session, url_for
from sqlalchemy import create_engine, text
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_table import Table, Col
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

# This is a sample of using Flask with MySQL to create a very basic web app.
# It is not secure nor fully functional. I've added instructional comments to
# help understand what is happening.
#
# It is assumed that the database is created independently. All queries to the
# database are written as strings and passed to `engine.execute(<query>)`
#
# Note that I am *not* a web developer. This is me learning about Flash and 
# web development so that we can create a demo app. I'm choosing simplicty over
# security and "correctness".

__author__ = 'Kevin Krenz'
__email__ = 'kevin.krenz@gmail.com'

# Create instance of Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'i34j29r8nvsi9h329835'

# Create connection to database. Yep, that's the username and password.
engine = create_engine('mysql://db_user:db_password@localhost/example_app')

# Make it look nice(r)! Start Bootstrap and create a navbar
nav = Nav()

@nav.navigation()
def navbar():
    return Navbar(View('Sample Web App','home'),
                   View('Users','users'),
                   View('Messages','messages'),
                   View('Login','login'),
                   View('Logout','logout'))

Bootstrap(app)
nav.init_app(app)

# PAGES
# For each page, create a function that returns a rendered template.
# Use a decorator for connecting it to a specific web page.
#
# Look in the templates folders for the templates.

@app.route('/')
def home():
    '''
    Returns a basically empty page.
    '''
    return render_template('home.html')


@app.route('/users')
def users():
    '''
    Display a list of all users in the database.
    '''

    # Execute the query
    # You can iterate through the results of a query and access column names
    # with row.<col_name>
    query = 'select * from users order by first_name,last_name'
    results = engine.execute(query)

    # Pass the query results to the template. In the template, you can access
    # the results with {{ user.<col_name> }}
    return render_template('show_users.html', users=results)


@app.route('/user/<username>')
def profile(username):
    '''
    Show information about the user.
    This function takes one argument, a piece of the URL. We can use that to
    query for that specific user.
    '''

    # Execute the query
    query = 'select * from users where username = \'%s\'' % username
    results = engine.execute(query)

    # Inappropriate number of users: flash a message and redirect to home.
    if results.rowcount <> 1:
        flash('Error looking up user %s' % username)
        return redirect('/')

    # Return rendered user profile.
    else:
        return render_template('user.html',user=results.first())

## FORMS
# Create a class that extends Form for each form you want.
# Include the fields you want, mark as required if needed.

class MessageForm(Form):
    '''
    Form for entering messages.
    '''
    message = TextField('Message: ', validators=[validators.required()])


@app.route('/messages', methods=['GET','POST'])
def messages():
    '''
    Allow user to add messages.
    Display all messages stored in database.
    '''

    # Istantiate the message form
    message_form = MessageForm(request.form)

    # If user submitted a message
    if request.method == 'POST':

        # Grab the message
        message = request.form['message']

        # Don't submit empty messages to the database
        if not message_form.validate():
            flash('Message is required.')
            return redirect('messages')

        # Update the database
        query = 'INSERT INTO messages (message) VALUES (\'%s\')' % message
        engine.execute(query)

    # Get all messages
    query = 'SELECT * FROM messages';
    results = engine.execute(query);

    # Create a table (HTML)
    class MessageTable(Table):
        message_id = Col('ID')
        message = Col('Message')

    table = MessageTable(results, border=True)

    # Return template with input form for new messages and table with all messages
    return render_template('messages.html', table=table, form=message_form)

## SESSIONS AND LOGINS

class LoginForm(Form):
    '''
    Simple login form. No authentication.
    '''
    username = TextField('Username: ', validators=[validators.required()])

@app.route('/login', methods=['GET','POST'])
def login():
    '''
    Simple login without authentication.
    Add username obtained from form to the session variable.
    '''
    # Instatiate the login form
    login_form = LoginForm(request.form)

    # User is attempting to login
    if request.method == 'POST':

        if login_form.validate():
            session['username'] = request.form['username']
            return redirect(url_for('home'))

        else:
            flash('Username is required.')
            return redirect(url_for('login'))

    # Method is GET, so display login form
    return render_template('login.html', form=login_form)

@app.route('/logout')
def logout():
    '''
    Logout by removing username from session variable.
    '''
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':

    # host=0.0.0.0 allows you to connect to the site from outside the VM
    app.run(debug=True, host='0.0.0.0', port=5000)
