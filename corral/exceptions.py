# -*- coding: utf-8 -*-
"""Custom exception classes."""

from werkzeug.exceptions import BadRequest, Forbidden


class SiteException(BadRequest):
    description = 'Received a non-200 status code.'


class NotAuthed(Forbidden):
    description = 'You must be authenticated.'
