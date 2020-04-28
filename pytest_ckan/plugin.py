# -*- coding: utf-8 -*-
import os
import sys

import pkg_resources

import pylons
from paste.deploy import loadapp
from pylons.i18n.translation import _get_translator


def pytest_addoption(parser):
    """Allow using custom config file during tests.
    """
    parser.addoption(u"--ckan-ini", action=u"store")


def pytest_sessionstart(session):
    """Initialize CKAN environment.
    """
    global pylonsapp
    path = os.getcwd()
    sys.path.insert(0, path)
    pkg_resources.working_set.add_entry(path)
    pylonsapp = loadapp(
        'config:' + session.config.option.ckan_ini,
        relative_to=path,
    )

    # Initialize a translator for tests that utilize i18n
    translator = _get_translator(pylons.config.get('lang'))
    pylons.translator._push_object(translator)

    class FakeResponse:
        headers = {}  # because render wants to delete Pragma
    pylons.response._push_object(FakeResponse)


def pytest_runtest_setup(item):
    """Automatically apply `ckan_config` fixture if test has `ckan_config`
    mark.

    `ckan_config` mark itself does nothing(as any mark). All actual
    config changes performed inside `ckan_config` fixture. So let's
    implicitely use `ckan_config` fixture inside any test that patches
    config object. This will save us from adding `@mark.usefixtures("ckan_config")`
    every time.
    """
    custom_config = [
        mark.args for mark in item.iter_markers(name=u"ckan_config")
    ]

    if custom_config:
        item.fixturenames.append(u"ckan_config")
