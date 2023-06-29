from flask import Blueprint, Flask
from markupsafe import escape

app = Flask(__name__)

routes_blueprint = Blueprint('api', __name__, url_prefix="/api/v1")


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"


@app.route('/tasks/<userid>', methods=["POST"])
def get_tasks(userid: int):
    return F'Tasks for user: {escape(userid)}'


routes_blueprint.add_url_rule('/', 'index', view_func=index)
routes_blueprint.add_url_rule(
    '/tasks/<userid>', 'get_tasks', view_func=get_tasks, methods=["POST"])

app.register_blueprint(routes_blueprint)
