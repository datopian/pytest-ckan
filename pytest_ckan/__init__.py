try:
    from ckan.tests.pytest_ckan.ckan_setup import *
except ImportError:
    from .impl.plugin import *
