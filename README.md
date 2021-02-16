# in-class 2021-02-10

docs:
* <http://flask.pocoo.org/docs/1.0/quickstart/>
* <https://devcenter.heroku.com/categories/python-support>
* <http://initd.org/psycopg/docs/usage.html>
* <https://github.com/silshack/flaskr/blob/master/flaskr.py>
* <https://developer.salesforce.com/blogs/developer-relations/2016/05/heroku-connect-flask-psycopg2.html>


### local setup:

```
# setup
pipenv install
pipenv shell
```

### heroku setup:

```
heroku create
heroku addons:create heroku-postgresql:hobby-dev
heroku config # take note of the DATABASE_URL
cp .env.example .env
# modify .env to have the DATABASE_URL
heroku pg:psql # run the commands in schema.sql
```

### Run remotely
```
git add .
git commit -m "setting up heroku"
git push heroku main
heroku open
```

### run locally
```
# setup
pipenv install
pipenv shell
heroku local dev
```

