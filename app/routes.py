from flask import jsonify
from .services import get_home, get_health, get_version


def register_routes(app):

    @app.route("/")
    def home():
        return jsonify(get_home())

    @app.route("/health")
    def health():
        return jsonify(get_health())

    @app.route("/version")
    def version():
        return jsonify({
            "version": get_version()
        })