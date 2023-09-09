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