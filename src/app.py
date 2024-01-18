from dotenv import load_dotenv
from flask import Flask, request, Response


load_dotenv()


def create_app(config=None):
    if config is None:
        config = {}
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route("/")
    def hello_world():
        return Response(response="<p>Hello, World!</p>")


app = create_app()
