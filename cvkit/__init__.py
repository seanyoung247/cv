
"""CV builder Flask application."""

from .views import blueprint
from .helpers import register_helpers

def init(app):
    """Register the CV builder with the Flask application."""
    app.register_blueprint(blueprint)
    register_helpers(app)
