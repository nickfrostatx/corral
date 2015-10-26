# -*- coding: utf-8 -*-
"""Custom exception classes."""

from werkzeug.exceptions import BadRequest, Forbidden


class SiteException(BadRequest):
    name = 'Received a non-200 status code'


class NotAuthed(Forbidden):
    name = 'You must be authenticated'
