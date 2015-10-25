# -*- coding: utf-8 -*-
"""Test the error handling."""

from flask import Flask, abort
import corral.error


def test_custom_handler():
    app = Flask(__name__)
    client = app.test_client()

    @corral.error.handle_errors(app, include_500=True)
    def handle(e):
        return e.name + '\n', e.code

    @app.route('/good')
    def good():
        return 'OK'

    @app.route('/404')
    def notfound():
        abort(404)

    @app.route('/internal')
    def divide_by_zero():
        1/0

    rv = client.get('/good')
    assert rv.status_code == 200

    rv = client.get('/404')
    assert rv.data == b'Not Found\n'
    assert rv.status_code == 404

    rv = client.get('/internal')
    assert rv.data == b'Internal Server Error\n'
    assert rv.status_code == 500


def test_html_handler():
    app = Flask(__name__, template_folder='../corral/templates')
    client = app.test_client()
    corral.error.register_html_handler(app, include_500=True)

    @app.route('/good')
    def good():
        return 'OK'

    @app.route('/404')
    def notfound():
        abort(404)

    @app.route('/internal')
    def divide_by_zero():
        1/0

    rv = client.get('/good')
    assert rv.status_code == 200

    rv = client.get('/404')
    assert b'<title>Corral - Not Found</title>' in rv.data
    assert b'Error 404' in rv.data
    assert rv.status_code == 404

    rv = client.get('/internal')
    assert b'<title>Corral - Internal Server Error</title>' in rv.data
    assert b'Error 500' in rv.data
    assert rv.status_code == 500
