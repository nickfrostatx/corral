# -*- coding: utf-8 -*-
"""These are the URL routes you can reach without auth."""

from flask import Blueprint, render_template, g
from ..util import detect_auth

public = Blueprint(__name__, 'public')
public.before_request(detect_auth)


@public.route('/', methods=['GET'])
def home():
    """Return either success or login page, depending on auth status."""
    if g.authed:
        return render_template('success.html')
    else:
        return render_template('login.html')
