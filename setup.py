import setuptools

VERSION = '0.9.1'

LONG_DESCRIPTION = open('README.rst').read()

CLASSIFIERS = [
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]

KEYWORDS = 'breakpoint debugging pdb print'

setuptools.setup(name='printbreakpoint',
                 version=VERSION,
                 description='Print breakpoint',
                 long_description=LONG_DESCRIPTION,
                 author='Duane Hilton',
                 author_email='duane9@gmail.com',
                 maintainer='Duane Hilton',
                 url='http://pypi.python.org/pypi/printbreakpoint/',
                 download_url='http://pypi.python.org/pypi/printbreakpoint/',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 classifiers=CLASSIFIERS,
                 python_requires='>=3.7',
                 keywords=KEYWORDS)
