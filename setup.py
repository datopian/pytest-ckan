from setuptools import setup

setup(
    name='pytest-ckan',
    packages=['pytest_ckan'],
    version=open('VERSION').read(),
    description='Backport of CKAN 2.9 pytest plugin and fixtures to CAKN 2.8',
    author='Shahar Evron',
    author_email='shahar.evron@datopian.com',
    install_requires=[],
)
