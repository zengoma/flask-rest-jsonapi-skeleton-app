# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
from api.views import api
from database import db, database_setup
from auth.permissions import permission_manager


# Create the Flask application
def create_app():
    _app = Flask(__name__)
    _app.config.from_object('config')
    db.init_app(_app)
    api.init_app(_app, Blueprint('api', __name__, url_prefix='/api'))
    api.permission_manager(permission_manager)
    return _app


def setup_database(_app):
    with _app.app_context():
        db.create_all()
        database_setup.populate_database()


app = create_app()
setup_database(app)


if __name__ == '__main__':
    # Start application
    app.run(debug=True)
