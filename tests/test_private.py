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


def test_cors(httpbin, tmpdir):
    app = create_app()
    app.config['SITES'] = {
        'site1': {
            'origin': httpbin.url,
            'filename': '%d.jpg',
            'path': str(tmpdir),
            'url': httpbin.url + '/status/%d',
        },
    }
    app.config['AUTH_KEY'] = 'secret'

    with app.test_client() as c:
        rv = c.post('/download/site1/123', headers={'Cookie': 'key=secret'})
        assert 'Access-Control-Allow-Origin' not in rv.headers

        rv = c.post('/download/site1/418', headers={'Origin': httpbin.url,
                                                    'Cookie': 'key=secret'})
        assert rv.headers.get('Access-Control-Allow-Origin') == httpbin.url
        assert rv.status_code == 400

        rv = c.post('/download/site1/418', headers={'Origin': 'http://goo.gl',
                                                    'Cookie': 'key=secret'})
        assert rv.headers.get('Access-Control-Allow-Origin') == httpbin.url
        assert rv.status_code == 400
