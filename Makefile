clean:
	rm -rf pypear/vim
	rm -rf pypear.egg-info
	rm -rf build
	rm -rf dist

submodules:
	git submodule update --init --recursive
	git submodule foreach git checkout master || :
	git submodule foreach git checkout main || :
	git submodule foreach git pull || :
	git add .

build: clean
	mkdir -p pypear/vim
	echo "Installing git-archive-all"
	pip install git-archive-all
	echo "Submodule init..."
	git submodule update --recursive --init
	echo "Creating vim plugin archive..."
	git archive-all pypear/vim/plugins.zip

install: build
	python setup.py install

dev: build
	pip install -e .

lint:
	flake8

test: lint
	pytest -s

dist: build test
	python setup.py sdist bdist_wheel

pypi: dist
	pip install twine
	python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
