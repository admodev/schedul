from flask import Blueprint


routes_blueprint = Blueprint('api', __name__, url_prefix="/api/v1")


def set_blueprint_for_routes(routes, app_def):
    for route in routes:
        routes_blueprint.add_url_rule(
            route["rule"], route["endpoint"], view_func=route["view_function"], methods=route["methods"])

    app_def.register_blueprint(routes_blueprint)
