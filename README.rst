Corral
======

.. image:: https://img.shields.io/travis/nickfrostatx/corral.svg
    :target: https://travis-ci.org/nickfrostatx/corral

.. image:: https://img.shields.io/coveralls/nickfrostatx/corral.svg
    :target: https://coveralls.io/github/nickfrostatx/corral

.. image:: https://img.shields.io/pypi/v/corral.svg
    :target: https://pypi.python.org/pypi/corral

.. image:: https://img.shields.io/pypi/l/corral.svg
    :target: https://raw.githubusercontent.com/nickfrostatx/corral/master/LICENSE

API for downloading files.

Installation
------------

.. code-block:: bash

    $ pip install nass

Usage
-----

This Flask server will download files from a specific configurable URL,
triggered by an API request. A POST request to the URL `/download/site1/729`
could be configured to initiate the download of a file from
`https://www.site1.com/download/729.jpg`. Basic cookie-based authentication
is provided using a master password. The password is sent in plain text, so
HTTPS is recommended.

See `config/config.py.sample` for a basic example.
