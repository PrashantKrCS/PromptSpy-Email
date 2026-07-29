from flask import Flask, render_template


def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    from web.api import api

    app.register_blueprint(api)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
