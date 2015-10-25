# -*- coding: utf-8 -*-
"""This module contains error handlers."""

from flask import render_template
from werkzeug.exceptions import HTTPException, InternalServerError
from functools import wraps

ERROR_CODES = (400, 401, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414,
               415, 416, 417, 418, 422, 423, 424, 426, 428, 429, 431, 501, 502,
               503, 504, 505)


def handle_errors(app, include_500=False):
    """Return a function decorator to catch all errors on app.

    :param include_500: If set to true, register a handler for 500
    """
    def wrapper(fn):
        """Register fn as an error handler for app."""
        @wraps(fn)
        def inner_handle(e):
            if not isinstance(e, HTTPException):
                e = InternalServerError()
            return fn(e)

        for status in ERROR_CODES:
            app.errorhandler(status)(inner_handle)
        if include_500:
            app.errorhandler(500)(inner_handle)

        return fn
    return wrapper


def html_handler(e):
    """Return an error page for exception e."""
    return render_template('error.html', e=e), e.code


def register_html_handler(app, include_500=False):
    """Register html error page as default error handler for app."""
    handle_errors(app, include_500)(html_handler)
