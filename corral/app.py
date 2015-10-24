# -*- coding: utf-8 -*-
"""Flask application factory."""

from flask import Flask


def create_app():
    """Return an instance of the Flask application."""
    # Create the app
    from . import __name__ as package_name
    app = Flask(package_name)

    # Handle all errors with an HTML error page
    from .error import register_html_handler
    register_html_handler(app, include_500=True)

    # Include all
    from .views import register_blueprints
    register_blueprints(app)

    return app
