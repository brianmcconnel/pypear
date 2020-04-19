clean:
	rm -rf vim-bundles
	rm -rf pypear.egg-info
	rm -rf build
	rm -rf dist


build: clean
	mkdir -p vim-bundles
	echo "Installing git-archive-all"
	pip install git-archive-all
	echo "Submodule init..."
	git submodule update --init
	echo "Creating vim plugin archive..."
	git archive-all vim-bundles/plugins.zip

install: build
	python setup.py install

dev: build
	pip install -e .

lint:
	flake8

test: lint
	pytest
