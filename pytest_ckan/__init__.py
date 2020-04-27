"""Plugin entrypoint

Prefer loading CKAN's built in pytest environment. If not found, fall back to
the implementation bundled in this package
"""

# flake8: noqa

try:
    from ckan.tests.pytest_ckan.ckan_setup import *
    from ckan.tests.pytest_ckan.fixtures import *
except ImportError:
    from pytest_ckan.plugin import *
    from pytest_ckan.fixtures import *
