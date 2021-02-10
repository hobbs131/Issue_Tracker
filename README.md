# in-class 2021-02-10

docs:
* <http://flask.pocoo.org/docs/1.0/quickstart/>
* <https://devcenter.heroku.com/categories/python-support>
* <http://initd.org/psycopg/docs/usage.html>
* <https://github.com/silshack/flaskr/blob/master/flaskr.py>
* <https://developer.salesforce.com/blogs/developer-relations/2016/05/heroku-connect-flask-psycopg2.html>


heroku setup:

```
heroku create
heroku addons:create heroku-postgresql:hobby-dev
# use `heroku config` to see environemnt variables, and setup a personal .env file
# see .env.example and make a .env file. Note the database URL can be copied directly from heroku's console.
git push heroku main
heroku open
```

local setup:

```
# setup
pipenv install
pipenv shell

# create .env with datastore connection params (see .env.example)
heroku pg:psql
# run schema.sql against the DB

# run
heroku local dev
```