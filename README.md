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

### Auth0 setup
1. You will need an auth0 account
2. You will need an auth0 application
3. You will need to configure your auth0 application on their website: <https://auth0.com/docs/quickstart/webapp/python/01-login>
    * If you want to test locally, you will need to configure an auth0 application to point locally. (i.e. `http://localhost:5000`)
    * If you want to run on heroku, you will need to look up your heroku urls and point auth0 to that.
    * I _think_ you can (mostly) configure one auth0 application to work for both, the only issue is that it seems auth0 only accepts one login url, (which can be left blank)
    * In this example, our logout url is `<domain>/` (we only redirect after logout to the home page), and our callback url is `<domain>/callback` .
4. update your `.env` file with auth0 related data (for local testing)
5. use `heroku config:set PARAM=VALUE` commands to update heroku's environment variables as well.

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

