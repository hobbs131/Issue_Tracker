# Upgrade of session 4 example. Now with heroku and postgressql
# in-class-09-19
heroku, postgres

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
# see .env.example and heroku control panel to build the DSN
heroku config:set DB_DSN="..."
git push heroku master
heroku open
```

local setup:

```
# setup
pipenv install
# create .env with datastore connection params (see .env.example)

# run
pipenv shell
heroku local dev
```

heroku commands:

```
heroku logs --tail
heroku pg
heroku pg:psql
```
