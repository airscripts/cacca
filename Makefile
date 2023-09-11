SHELL = /bin/bash

.SUFFIXES:
.SUFFIXES: .sh

.PHONY: setup
setup:
	bash scripts/setup.sh

.PHONY: build
build: setup
	bash scripts/build.sh

.PHONY: publish.npm
publish.npm: build
	bash scripts/publish.npm.sh

.PHONY: publish.pypi
publish.pypi: build
	bash scripts/publish.pypi.sh

.PHONY: code.install
code.install:
	bash scripts/code.install.sh

.PHONY: code.uninstall
code.uninstall:
	bash scripts/code.uninstall.sh