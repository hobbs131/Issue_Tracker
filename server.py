from flask import Flask, render_template, request, g, redirect, url_for, jsonify, abort

import db

app = Flask(__name__)

# have the DB submodule set itself up before we get started. groovy.
@app.before_first_request
def initialize():
    db.setup()

@app.route('/')
def home():
    user_name = request.args.get("userName", "unknown")
    return render_template('main.html', user=user_name)

@app.route('/people', methods=['GET'])
def people():
    with db.get_db_cursor() as cur:
        cur.execute("SELECT * FROM person;")
        names = [record[1] for record in cur]

        return render_template('people.html', user=user_name)

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
        cur.execute("SELECT name from person where person_id = %s;", (id,))
        names = [record[0] for record in cur];
        if(len(names) == 0):
            return abort(404)
        else:
            return render_template("person.html", name=names[0], id=id)


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

