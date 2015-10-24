# -*- coding: utf-8 -*-
"""Helper functions for file downloading."""

from requests import get
from .exceptions import SiteException


def download(url, path):
    """Download the file at url to path."""
    r = get(url, allow_redirects=False, stream=True)
    if r.status_code != 200:
        raise SiteException()
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
