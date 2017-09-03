except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Brendan Davis',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'brendanmd@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)