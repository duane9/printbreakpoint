#!/usr/bin/env python
from distutils.core import setup

LONG_DESCRIPTION = open('README.md').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'dbugging pdb breakpoint print'

setup(name='pd',
      version='0.9',
      description='Print debugging with Python 3 breakpoint.',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/md',
      author='Duane Hilton',
      author_email='duane9@gmail.com',
      maintainer='Duane Hilton',
      download_url='http://pypi.python.org/pypi/pd/',
      packages=['pd'],
      package_dir={'pd': 'pd'},
      platforms=['Platform Independent'],
      license='MIT',
      classifiers=CLASSIFIERS,
      python_requires='>=3.7',
      keywords=KEYWORDS)
