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
    * The "communication" in auth0 occurs mostly in the client browser -- so you don't really need to tell auth0 where your server is, just where you're browser accesses it.
    * If you want to test locally, you will need to configure an auth0 application to point locally. (i.e. `http://localhost:5000`)
    * If you want to run on heroku, you will need to look up your heroku urls and point auth0 to that.
    * In this example, our login url is `<domain>/login`, our logout url is `<domain>/` (we only redirect after logout to the home page), and our callback url is `<domain>/callback` 
        * In testing I was finding auth0 to not like `localhost:5000/login` as an "Application Login URI" -- it seems OK with this being left blank.
4. update your `.env` file with auth0 related data (for local testing)
5. use `heroku config:set PARAM=VALUE` commands to update heroku's environment variables as well. These probably will not match those in your `.env` file.

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

