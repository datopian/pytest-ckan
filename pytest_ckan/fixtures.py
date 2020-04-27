try:
    from ckan.tests.pytest_ckan.fixtures import *
except ImportError:
    from .impl.fixtures import *
