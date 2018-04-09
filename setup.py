from distutils.core import setup
setup(
        name = 'hypnolog-python',
        packages = ['hypnolog-python'], # this must be the same as the name above
        version = '0.1',
        description = 'Python wrapper for quick logging using HypnoLog',
        author = 'SimonLdj',
        author_email = 'simon.ldj@gmail.com',
        url = 'https://github.com/SimonLdj/hypnolog-python',
        download_url = 'https://github.com/SimonLdj/hypnolog-python/archive/v0.1.tar.gz',
        keywords = ['hypnolog', 'debugging', 'debug', 'log', 'logging', 'console', 'visualization'],
        classifiers = [],
        install_requires=[
            'requests',
            'jsonpickle',
            ],
        )
