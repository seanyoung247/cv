
"""CV builder Flask application."""

from .views import blueprint


def init(app):
    """Register the CV builder with the Flask application."""
    app.register_blueprint(blueprint)
