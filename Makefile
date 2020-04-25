clean:
	rm -rf pypear/vim
	rm -rf pypear.egg-info
	rm -rf build
	rm -rf dist


build: clean
	mkdir -p pypear/vim
	echo "Installing git-archive-all"
	pip install git-archive-all
	echo "Submodule init..."
	git submodule update --init
	echo "Creating vim plugin archive..."
	git archive-all pypear/vim/plugins.zip

install: build
	python setup.py install

dev: build
	pip install -e .

lint:
	flake8

test: lint
	pytest

pypi: build
	python setup.py sdist bdist_wheel
	pip install twine
	python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
