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
		return redirect('/issues')
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
		cur.execute("SELECT json_agg(issues) FROM issues WHERE deletedAt IS NULL")
		results = cur.fetchone()[0]
		if (results != None):
			return render_template('issues.html', results=results)
		return render_template('issues.html')


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
		return redirect('/issues')
@app.route('/edit_issue', methods = ["POST"])
def editIssueEntry():
	with db.get_db_cursor(True) as cur:
		id = int(request.form.get('id'))
		issue = request.form.get('issue')
		priority = request.form.get('priority')
		opened_on = request.form.get('opened_on')
		opened_by = request.form.get('opened_by')
		assignee = request.form.get('assignee')
		closed_on = request.form.get('closed_on')
		closed_by = request.form.get('closed_by')
		status = request.form.get('status')
		print("DEBUG: (\""+str(id)+"\",\""+issue+"\",\""+priority+"\",\""+opened_on+"\",\""+opened_by+"\",\""+assignee+"\",\""+closed_on+"\",\""+closed_by+"\",\""+status+"\")");
		cur.execute("UPDATE issues SET issue=%s, priority = %s, opened_on = %s, opened_by = %s, assignee = %s, closed_on = %s, closed_by = %s, status = %s WHERE id = %s", (issue, priority, opened_on, opened_by, assignee, closed_on, closed_by, status,id))


@app.route('/delete', methods = ["POST"])
def deleteIssueEntry():
	with db.get_db_cursor(True) as cur:
		data = request.json
		id = data['issueId']
		cur.execute("UPDATE issues SET  deletedAt = now()  WHERE  id = %s" % id)
		return ""
