try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Zero Inflated Factor Analysis',
    'author': 'Emma Pierson and Christopher Yau',
    'url': 'https://github.com/epierson9/ZIFA',
    'package_dir':{'zifa': 'zifa'},
    #'download_url': '',
    'author_email': 'emmap1@cs.stanford.edu',
    'version': '0.1',
    'install_requires': ['pylab','sklearn','scipy','numpy',''],
    'packages': ['zifa'],
    'name': 'ZIFA',
    'test_suite':"tests",
    'license':"MIT"
}

setup(**config)

#>> python setup.py test