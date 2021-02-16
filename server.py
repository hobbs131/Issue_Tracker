from flask import Flask, render_template, request, g, redirect, url_for, jsonify, abort, session
from urllib.parse import urlencode
import os
import db
from auth0 import auth0_setup, require_auth, auth0



app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET_KEY"]

# have the DB submodule set itself up before we get started. groovy.
@app.before_first_request
def initialize():
    db.setup()
    auth0_setup()



### AUTH:
@app.route('/login')
def login():
    if 'profile' in session:
        return redirect(url_for('test_auth'))
    else:
        return auth0().authorize_redirect(redirect_uri=url_for('callback', _external=True))

@app.route('/logout')
def logout():
    session.clear()
    params = { 'returnTo': url_for('home', _external=True), 'client_id': os.environ['AUTH0_CLIENT_ID'] }
    return redirect(auth0().api_base_url + '/v2/logout?' + urlencode(params))

@app.route('/callback')
def callback():
    auth0().authorize_access_token()
    resp = auth0().get('userinfo')
    userinfo = resp.json()

    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }

    return redirect('/test_auth')

@app.route('/test_auth')
@require_auth
def test_auth():
    return render_template("test_auth.html", profile=session['profile'])






@app.route('/')
def home():
    user_name = request.args.get("userName", "unknown")
    return render_template('main.html', user=user_name)

@app.route('/people', methods=['GET'])
def people():
    with db.get_db_cursor() as cur:
        cur.execute("SELECT name FROM person;")
        names = [record[0] for record in cur]

        return render_template('people.html', names=names)

@app.route('/people', methods=['POST'])
def new_person():
    with db.get_db_cursor(True) as cur:
        name = request.form.get("name", "unnamed friend")
        app.logger.info("Adding person %s", name)
        cur.execute("INSERT INTO person (name) values (%s)", (name,))
        
        return redirect(url_for('people'))


@app.route('/people/<int:id>', methods=['GET'])
def get_person(id):
    with db.get_db_cursor(False) as cur:
        cur.execute("SELECT name, description from person where person_id = %s;", (id,))
        people = [record for record in cur];
        if(len(people) == 0):
            return abort(404)
        else:
            return render_template("person.html", name=people[0][0], desc=people[0][1], id=id)

@app.route('/people/<int:id>', methods=['POST'])
def edit_person(id):
    description = request.form.get("description")
    with db.get_db_cursor(True) as cur:
        cur.execute("UPDATE person set description = %s where person_id = %s;", (description, id))
        return redirect(url_for("get_person", id=id))

@app.errorhandler(404)
def error404(error):
    return "oh no. you killed it."


@app.route('/api/foo')
def api_foo():
    data = {
        "message": "hello, world",
        "isAGoodExample": False,
        "aList": [1, 2, 3],
        "nested": {
            "key": "value"
        }
    }
    return jsonify(data)

