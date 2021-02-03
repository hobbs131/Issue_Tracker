import os
from flask import Flask, render_template, request, g
app = Flask(__name__)


def connect_db():
    """Connects to the specific database."""
    return psycopg2.connect(os.environ.get('DB_DSN'))

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'pg_db'):
        g.pg_db = connect_db()
    return g.pg_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.pg_db.close()

@app.route('/')
def hello_world():
    user_name = request.args.get("userName", "unknown")
    return render_template('main.html', user=user_name)

@app.route('/people')
def people():
    conn = get_db()

    cur = conn.cursor()
    cur.execute("SELECT * FROM person;")
    names = [record[1] for record in cur]
    cur.close()

    return render_template("people.html", names=names)
