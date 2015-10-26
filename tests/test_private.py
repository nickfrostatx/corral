# -*- coding: utf-8 -*-
"""Test the private routes."""

from corral.app import create_app
import json


def test_auth():
    app = create_app()
    app.config['SITES'] = {}
    app.config['AUTH_KEY'] = 'secret'

    with app.test_client() as c:
        rv = c.post('/download/site1/123')
        data = json.loads(rv.data.decode('utf-8'))
        assert data['msg'] == 'You must be authenticated'
        assert rv.status_code == 403

        rv = c.post('/download/site1/123', headers={'Cookie': 'key=abc'})
        data = json.loads(rv.data.decode('utf-8'))
        assert data['msg'] == 'You must be authenticated'
        assert rv.status_code == 403

        rv = c.post('/download/site1/123', headers={'Cookie': 'key=secret'})
        data = json.loads(rv.data.decode('utf-8'))
        assert data['msg'] == 'Not Found'
        assert rv.status_code == 404
