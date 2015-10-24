# -*- coding: utf-8 -*-
"""
This module contains all the view blueprints.

When adding a new view blueprint, make sure to add it to
register_blueprints.
"""


def register_blueprints(app):
    """Register all blueprints to app."""
    from .public import public
    app.register_blueprint(public)

    from .private import private
    app.register_blueprint(private)
