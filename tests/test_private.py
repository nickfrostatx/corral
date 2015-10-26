# -*- coding: utf-8 -*-
"""Test the private routes."""

from corral.app import create_app
import json


def test_auth():
    app = create_app()
    app.config['SITES'] = {}
    app.config['AUTH_KEY'] = 'secret'
    app.config['DEBUG'] = True

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
            'filename': '{}.jpg',
            'path': str(tmpdir),
            'url': httpbin.url + '/status/418',
        },
    }
    app.config['AUTH_KEY'] = 'secret'
    app.config['DEBUG'] = True

    with app.test_client() as c:
        rv = c.post('/download/site1/123', headers={'Cookie': 'key=secret'})
        assert 'Access-Control-Allow-Origin' not in rv.headers

        rv = c.post('/download/site1/123', headers={'Origin': httpbin.url,
                                                    'Cookie': 'key=secret'})
        assert rv.headers.get('Access-Control-Allow-Origin') == httpbin.url
        assert rv.status_code == 400

        rv = c.post('/download/site1/123', headers={'Origin': 'http://goo.gl',
                                                    'Cookie': 'key=secret'})
        assert rv.headers.get('Access-Control-Allow-Origin') == httpbin.url
        assert rv.status_code == 400


def test_download(httpbin, tmpdir):
    app = create_app()
    app.config['SITES'] = {
        'site1': {
            'origin': httpbin.url,
            'filename': '{}.jpg',
            'path': str(tmpdir),
            'url': httpbin.url + '/bytes/1024',
        },
    }
    app.config['AUTH_KEY'] = 'secret'
    app.config['DEBUG'] = True

    with app.test_client() as c:
        rv = c.post('/download/site1/123', headers={'Cookie': 'key=secret'})
        assert tmpdir.join('123.jpg').size() == 1024
        assert rv.data == b'{}'
        assert rv.status_code == 200
