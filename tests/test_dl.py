# -*- coding: utf-8 -*-
"""Test downloading."""

import corral.dl
import corral.exceptions
import os
import pytest
import requests


def test_dl(httpbin, tmpdir):
    path = tmpdir.join('out.bin')
    corral.dl.download(httpbin.url + '/stream-bytes/1024', str(path))
    assert path.size() == 1024


def test_bad_status(httpbin, tmpdir):
    path = tmpdir.join('out.bin')
    with pytest.raises(corral.exceptions.SiteException) as exc:
        corral.dl.download(httpbin.url + '/status/403', str(path))
