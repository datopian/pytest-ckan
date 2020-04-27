# Automate all the things

SHELL := bash
PYTHON := python
PIP := pip
GIT := git

VERSION_FILE = VERSION
BUILD_DIR := build
DIST_DIR := dist
SENTINELS := .make-cache

VERSION := $(shell cat $(VERSION_FILE))
SOURCE_FILES := $(shell find ./pytest_ckan -type f -name "*.py")

## Clean all generated files
distclean:
	rm -rf $(BUILD_DIR) $(DIST_DIR)
	rm -rf $(SENTINELS)/dist
.PHONY: distclean

## Create distribution files to upload to pypi
dist: $(SENTINELS)/dist
.PHONY: dist

## Upload a release of the package to PyPi and create a Git tag
release: $(SENTINELS)/dist
	@echo
	@echo "You are about to release authoritah version $(VERSION)"
	@echo "This will:"
	@echo " - Create a git tag release-$(VERSION)"
	@echo " - Create a release package and upload it to pypi"
	@echo
	@echo "Continue? (hit Enter or Ctrl+C to stop"
	@read
	$(GIT) tag release-$(VERSION)
	$(GIT) push --tags
	$(PYTHON) -m twine upload dist/*
.PHONY: release

$(SENTINELS):
	mkdir $@

$(SENTINELS)/dist-setup: | $(SENTINELS)
	$(PIP) install -U pip wheel twine
	@touch $@

$(SENTINELS)/dist: $(SENTINELS)/dist-setup $(DIST_DIR)/pytest-ckan-$(VERSION).tar.gz $(DIST_DIR)/pytest_ckan-$(VERSION)-py2.py3-none-any.whl | $(SENTINELS)
	@touch $@

$(DIST_DIR)/pytest-ckan-$(VERSION).tar.gz $(DIST_DIR)/pytest_ckan-$(VERSION)-py2.py3-none-any.whl: $(SOURCE_FILES) setup.py | $(SENTINELS)/dist-setup
	$(PYTHON) setup.py sdist bdist_wheel --universal
