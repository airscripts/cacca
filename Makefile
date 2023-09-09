SHELL = /bin/sh

.SUFFIXES:
.SUFFIXES: .sh

.PHONY: setup
setup:
	sh scripts/setup.sh

.PHONY: build
build: 
	sh scripts/build.sh