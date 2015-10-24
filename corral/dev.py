# -*- coding: utf-8 -*-
"""Development app runner."""


def run():
    """Run app in the development environment.

    Don't call this in production.
    """
    from .app import create_app
    app = create_app()
    app.config.from_envvar('CORRAL_SETTINGS')
    return app.run()
