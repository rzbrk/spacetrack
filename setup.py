import re

from setuptools import setup, find_packages


INIT_FILE = 'spacetrack/__init__.py'
init_data = open(INIT_FILE).read()

metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", init_data))

VERSION = metadata['version']
LICENSE = metadata['license']
DESCRIPTION = metadata['description']
AUTHOR = metadata['author']
EMAIL = metadata['email']

requires = [
    'httpx',
    'logbook>=0.12.3',
    'python-dateutil',
    'represent>=1.4.0',
    'rush',
    'sniffio',
]

extras_require = dict()

extras_require['test'] = [
    'pytest-asyncio',
    'pytest-trio',
    'pytest>=6.0',
    'respx',
]

extras_require['docstest'] = [
    'doc8',
    'pyenchant',
    'sphinx',
    'sphinx_rtd_theme',
    'sphinxcontrib-spelling',
]

extras_require['pep8test'] = [
    'flake8',
    'flake8-future-import',
    'pep8-naming',
]


setup(
    name='spacetrack',
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.rst').read(),
    author=AUTHOR,
    author_email=EMAIL,
    url='https://github.com/python-astrodynamics/spacetrack',
    project_urls={
        "Documentation": "https://spacetrack.readthedocs.io/",
    },
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license=LICENSE,
    install_requires=requires,
    python_requires='>=3.6',
    extras_require=extras_require)
