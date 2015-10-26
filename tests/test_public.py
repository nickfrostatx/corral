# -*- coding: utf-8 -*-
"""Test the public routes."""

from corral.app import create_app


def test_root():
    app = create_app()
    app.config['AUTH_KEY'] = 'secretpassword'

    with app.test_client() as c:
        rv = c.get('/')
        assert b'<h1>Login</h1>' in rv.data
        assert rv.status_code == 200

        rv = c.get('/', headers={'Cookie': 'key=abc'})
        assert b'<h1>Login</h1>' in rv.data
        assert rv.status_code == 200

        rv = c.get('/', headers={'Cookie': 'key=secretpassword'})
        assert b'>Authenticated</h1>' in rv.data
        assert rv.status_code == 200
