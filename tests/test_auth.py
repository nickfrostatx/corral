# -*- coding: utf-8 -*-
"""Test authentication functions."""

from flask import Flask, g, jsonify
import corral.util
import json


def test_detect_auth():
    app = Flask(__name__)
    app.config['AUTH_KEY'] = 'secretpassword'

    app.before_request(corral.util.detect_auth)

    @app.route('/checkauth')
    def check_auth():
        return jsonify({'authed': g.authed})

    with app.test_client() as c:
        rv = c.get('/checkauth')
        data = json.loads(rv.data.decode('utf-8'))
        assert data['authed'] == False

        rv = c.get('/checkauth', headers={'Cookie': 'key=secretpassword'})
        data = json.loads(rv.data.decode('utf-8'))
        assert data['authed'] == True


def test_enforce_auth():
    app = Flask(__name__)
    app.config['AUTH_KEY'] = 'secretpassword'

    app.before_request(corral.util.enforce_auth)

    @app.route('/admin')
    def admin_panel():
        return 'Admin panel.\n'

    with app.test_client() as c:
        rv = c.get('/admin')
        assert b'You must be authenticated' in rv.data
        assert rv.status_code == 403

        rv = c.get('/admin', headers={'Cookie': 'key=secretpassword'})
        assert rv.data == b'Admin panel.\n'
        assert rv.status_code == 200
