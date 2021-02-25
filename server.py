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
        return redirect(url_for('issues'))
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

    return redirect('/issues')

@app.route('/')
def home():
     return redirect(url_for('login'))

@app.route('/issues')
def issues():
	with db.get_db_cursor(True) as cur:
		cur.execute("SELECT json_agg(issues) FROM issues")
		results = cur.fetchone()[0]
		if (results != None):
			return render_template('issues.html', results=results)

@app.route('/add_issue')
def add_issue():
    return render_template('add_issue.html')

@app.route('/postIssueEntry', methods = ["POST"])
def postIssueEntry():
	with db.get_db_cursor(True) as cur:
		issue = request.form.get('issue')
		priority = request.form.get('priority')
		opened_on = request.form.get('opened_on')
		opened_by = request.form.get('opened_by')
		assignee = request.form.get('assignee')
		closed_on = request.form.get('closed_on')
		closed_by = request.form.get('closed_by')
		status = request.form.get('status')
		cur.execute("INSERT INTO issues (issue, priority, opened_on, opened_by, assignee, closed_on, closed_by, status) values (%s,%s,%s,%s,%s,%s,%s,%s)", (issue, priority, opened_on, opened_by, assignee, closed_on, closed_by, status,))
		cur.execute("SELECT json_agg(issues) FROM issues")
		results = cur.fetchone()[0]
		return render_template('issues.html', results=results)


