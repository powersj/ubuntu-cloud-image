PYTHON = python3
SETUP  := $(PYTHON) setup.py

.PHONY: clean install publish snap test venv

clean:
	$(SETUP) clean
	rm -f .coverage *.snap *.tar.bz2
	rm -rf build/ dist/ prime/ stage/ htmlcov/
	rm -rf *.eggs/ *.egg-info/ .pytest_cache/ .tox/
	@find . -regex '.*\(__pycache__\|\.py[co]\)' -delete

install:
	pip install -r requirements.txt
	$(SETUP) install

publish:
	rm -rf dist/
	$(SETUP) sdist
	pip install twine
	twine upload dist/*

snap:
	snapcraft cleanbuild --debug

test:
	pytest --cov=ubuntu_cloud_image ubuntu_cloud_image
	flake8 --max-line-length=88 ubuntu_cloud_image setup.py
	black --check .

venv:
	$(PYTHON) -m virtualenv -p /usr/bin/$(PYTHON) .venv
	.venv/bin/pip install -Ur requirements.txt -Ur requirements-test.txt
	@echo "Now run the following to activate the virtual env:"
	@echo ". .venv/bin/activate"
