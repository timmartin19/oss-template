.. highlight:: shell

CLI Interface
=============

There are three major groups of commands in this project

* bin/*
    These bash scripts should be run locally (not in docker).  They are primarily dev tools
* image/*
    These are bash scripts designed to be run from within the docker container.  They are added directly to the docker image
* Flask commands
    Commands explicitly hooked into Flask's CLI feature.  They typically are specifically tied
    to the application rather than being dev only commands

Local Commands
--------------

* `bin/build-docs`: Builds and opens the documentation in your browser
* `bin/setup-osx`: Installs and initializes pyenv, virtualenv, and virtualenvwrapper for local development

In-Docker Commands:
-------------------

When you are running these in Docker you can simply call them directly
by their name as the `image/` directory is added to the `PATH` env var:
e.g. `test-unit` instead of `image/test-unit`

* `image/forever`: Executes the arguments and re-runs them every time something in the repo changes.
    Example `forever test-unit` will run the unit tests every time it detects a change
* `image/lint`: Runs pylint, giving you static analyisis and style checking
* `image/run-app`: Runs the application using uwsgi
* `image/test-all`: Runs all tests and the linter
* `image/test-coverage`: Runs the tests and outputs the coverage statistics
* `image/test-unit`: Runs the unit tests only

Flask Commands
--------------

To run these commands you need to set the `FLASK_APP`.  Simply passing
the wsgi module should work: e.g. `export FLASK_APP={{ cookiecutter.project_slug }}.wsgi`
should be sufficient.  The Docker image has already appropriately set the `FLASK_APP` env var.

To run these commands in the docker image simply do `docker-compose run app <command>`

* `flask version`: Displays the app version and other relevant info
* `flask shell`: Start a python shell from within the `Flask application context <http://flask.pocoo.org/docs/0.11/appcontext/>`_

Adding Flask Commands
"""""""""""""""""""""

If you wish to add your own custom app commands, simply edit
the {{ cookiecutter.project_slug }}/cli.py file with the desired
command.  See the `click documentation <http://click.pocoo.org>`_
for more information.
