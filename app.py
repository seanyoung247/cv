
"""Application entry point."""

from flask import Flask

import cvkit


def create_app():
    app = Flask(__name__)

    cvkit.init(app)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
