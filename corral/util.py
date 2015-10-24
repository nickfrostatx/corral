# -*- coding: utf-8 -*-
"""Utilty authentication functions."""

from flask import current_app, request, g
from werkzeug.exceptions import Forbidden
from werkzeug.security import safe_str_cmp
from .exceptions import NotAuthed


def detect_auth():
    """Determine whether the user has the correct auth cookie set."""
    g.authed = safe_str_cmp(request.cookies.get('key', ''),
                            current_app.config['AUTH_KEY'])


def enforce_auth():
    """Raise a 403 if the user isn't authenticated."""
    detect_auth()
    if not g.authed:
        raise NotAuthed()
