# -*- coding: utf-8 -*-
"""These JSON-formatted views require authentication."""

from flask import Blueprint, jsonify, request, current_app, g
from werkzeug.exceptions import NotFound
from os.path import join
from ..dl import download
from ..error import handle_errors
from ..util import enforce_auth

private = Blueprint(__name__, 'private')
private.before_request(enforce_auth)


@handle_errors(private)
def json_error(e):
    """Return an error response like {"msg":"Method not allowed"}."""
    return jsonify({'msg': e.description})


@private.route('/download/<site_id>/<int:param>', methods=['POST'])
def home(site_id, param):
    """Attempt to download the file."""
    if site_id in current_app.config['SITES']:
        site = current_app.config['SITES'][site_id]
        g.site = site
        url = site['url'].format(param)
        filename = site['filename'].format(param)
        path = join(site['path'], filename)
        download(url, path)
        return jsonify({})
    raise NotFound


@private.after_request
def cors(response):
    """Handle browser cross-origin requests."""
    if 'origin' in request.headers:
        site = g.get('site')
        if site:
            allowed_origin = site['origin']
            response.headers['Access-Control-Allow-Origin'] = allowed_origin
    return response
