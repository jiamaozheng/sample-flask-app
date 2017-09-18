# A Sample Web App with Flask

This is a sample of using Flask with MySQL to create a very basic web app. It is not secure nor fully functional. I've added instructional comments to help understand what is happening.

It is assumed that the database is created independently. All queries to the database are written as strings and passed to `engine.execute(<query>)`. I'm working on this primarily for a databases class, so I'm not bothering with ORM or executing similar queries with Python functions. That would be better, but it doesn't match the needs for the class.

Also note that I am *not* a web developer. This is me learning about Flask and web development so that we can create a demo app. I'm choosing simplicty over security and "correctness".

## How does Flask work?

This is going to be a very high-level description -- there are plenty of tutorials out there for actual details. And again, I'm not a web developer -- this is probably overly simplified and partially wrong.

Anyway, with Flask, you can write functions that grab all of the data you need to pass to the page. This could be simple calculations, or you could connect to a database and do whatever processing is needed. You then use Python decorators for these functions to map them to a specific web page.

Once you have all of the data you need in a function, you need to put this in a format that works for a web page, i.e. HTML. To do this, you create some templates in the `templates/` folder, and then call `render_template(<template.html>,data, ...)`.

The templates use [Jinja](http://jinja.pocoo.org). This allows you use to use a Python-like syntax for creating HTML. For examples, you can pass a list of dictionaries to Jinja, and in the template, do something like this:

```html
<ul>
{% for row in rows %}
    <li>{{ row.first_name }} ({{ row.username }})</li>
{% endfor %}
</ul>
```

This would then created a bulleted list of users, where each line is like "Kevin (kevin_krenz)".

## Pre-requisites

### Ubuntu

This sample app doesn't need to run on Ubuntu, but I don't know what other dependencies you'll need to install. If you are running Ubuntu, this command should get you all of the dependencies you need:

```
$ sudo apt install mysql-server mysql-client libmysqlclient-dev python-dev
```

### MySQL

Have an instance of MySQL running. Run the `create_database.sql` file to create the example database, database user, table, and populate the table with a few rows. To do this, login as the root user (or an admin user):

```
$ mysql -u <user> -p
```

This will ask for the password. Once you're in MySQL, run the script:

```
mysql> source <path_to_script>/create_database.sql;
```

### Python

Install the following Python modules:

- Flask
- SQL Alchemy
- WTForms
- Flask Table

You can do this with the following command:

```
$ pip install Flask SQLAlchemy MySQLdb-python WTForms flask-table
```

If I'm missing anything here, let me know.

## Running the app

Move to the directory and run the following command:

```
$ python main.py
```

## Tinkering

Again, this is for learning! Once you have things running, start tinkering. Change queries, update the templates, modify the database, etc.

## TODO

- [ ] Better theme
- [ ] Sortable table
- [ ] Button to modify/delete message
