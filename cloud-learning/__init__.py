import os

from flask import Flask
import click
from . import submit, download
from .utils import load_datasets_from_remote

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Check server health
    @app.route('/ping')
    def ping():
        return 'Pong!'

    # Blue Prints
    app.register_blueprint(submit.bp)
    app.register_blueprint(download.bp)
    # Commands
    @app.cli.command('install_datasets', help='Install datasets')
    def datasets():
        load_datasets_from_remote()
    return app