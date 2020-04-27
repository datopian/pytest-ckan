"""Plugin entrypoint

Prefer loading CKAN's built in pytest environment. If not found, fall back to
the implementation bundled in this package
"""

try:
    from ckan.tests.pytest_ckan.ckan_setup import *
    from ckan.tests.pytest_ckan.fixtures import *
except ImportError:
    from .impl.plugin import *
    from .impl.fixtures import *
