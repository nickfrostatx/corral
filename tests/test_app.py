# -*- coding: utf-8 -*-
"""Test the scaffolding of the app."""

from flask import Flask
import corral.app


def test_app():
    app = corral.app.create_app()
    assert isinstance(app, Flask)
