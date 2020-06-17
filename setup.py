from os import path
from setuptools import setup


# Get the long description from the relevant file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='pytest-ckan',
    packages=['pytest_ckan'],
    version=open('VERSION').read(),
    description='Backport of CKAN 2.9 pytest plugin and fixtures to CAKN 2.8',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Shahar Evron',
    author_email='shahar.evron@datopian.com',
    copyright='Copyright 2020 (c) Viderum Inc. / Datopian',
    license = 'MIT',
    url='https://github.com/datopian/pytest-ckan',
    install_requires=[
        'mock',
        'pytest',
    ],
    entry_points={"pytest11": ["ckan = pytest_ckan"]},
    keywords = ['ckan', 'pytest'],
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
)
