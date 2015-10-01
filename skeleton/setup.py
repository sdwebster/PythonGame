try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'My Project',
  'author': 'Steve Webster',
  'url': '[where to get at it]',
  'download_url': '[where to download it]',
  'author_email': 'stephendwebster@gmail.com',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'My Project'
}

setup(**config)
