# -*- coding: utf-8 -*-

from setuptools import setup
import re

version = ''
with open('corral/__init__.py', 'r') as f:
    version = re.search(r'__version__\s*=\s*\'([\d.]+)\'', f.read()).group(1)

with open('README.rst') as f:
    readme = f.read()

with open('HISTORY.rst') as f:
    history = f.read()

setup(
    name='corral',
    version=version,
    author='Nick Frost',
    author_email='nickfrostatx@gmail.com',
    url='https://github.com/nickfrostatx/corral',
    description='API for downloading files.',
    long_description=readme + '\n\n' + history,
    packages=[
        'corral',
        'corral.views',
    ],
    package_data={'corral': ['templates/*.html']},
    install_requires=[
        'Flask>=0.10.1',
        'requests>=2.7.0',
    ],
    entry_points={
        'console_scripts': [
            'corral-run = corral.dev:run',
        ],
    },
    license='MIT',
    keywords='corral',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
