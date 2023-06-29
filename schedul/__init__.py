# Library imports
from flask import Flask
from markupsafe import escape

# User defined imports
from schedul.config.server_config import set_blueprint_for_routes

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/tasks/<userid>', methods=["POST"])
def get_tasks(userid: int):
    return F'Tasks for user: {escape(userid)}'


routes_definition = [{'rule': '/', 'endpoint': 'index',
                      'view_function': index, 'methods': ["GET"]},
                     {'rule': '/tasks/<userid>', 'endpoint': 'get_tasks',
                      'view_function': get_tasks, 'methods': ["POST"]}]

set_blueprint_for_routes(routes_definition, app)
