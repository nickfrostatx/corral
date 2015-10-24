test:
	py.test -v --pep8 --cov=corral --cov-report=term-missing

test-257:
	py.test -v --pep8 --cov=corral --cov-report=term-missing

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload

install:
	pip install -e .
	pip install pytest pytest-cov pytest-pep8 pytest-pep257
