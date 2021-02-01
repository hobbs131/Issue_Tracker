# "Dummy" project for quickly playing around with Flask.

See [the flask quickstart guide](http://flask.pocoo.org/docs/1.0/quickstart/)

To run: `FLASK_APP=server.py FLASK_ENV=development flask run` (one big command)

* hello world: 
	*`Flask(__name__)` sets up a flask server
	* `@app.route("/")` uses python's declerator syntax to register this function to a url route.
	* logging: `app.logger.info(...)`
	* static content: add image to static folder.
	* from template: `render_template("foo.html")`
	* extracting info from request: `request.args["foo"]` (or `args.get(..., default)` if it's optional...
	* add conditional rendering to template: `{% if property %} ... {% endif %}`
	* templated additions `{{ variable }}`
