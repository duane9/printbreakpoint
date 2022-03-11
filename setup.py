import setuptools

VERSION = '0.9.8'

LONG_DESCRIPTION = open('README.rst').read()

CLASSIFIERS = [
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
]

KEYWORDS = 'print breakpoint debugging pdb'

DESCRIPTION = 'Use breakpoint() to print out filename, line number, and data.'

setuptools.setup(name='printbreakpoint',
                 version=VERSION,
                 description=DESCRIPTION,
                 long_description=LONG_DESCRIPTION,
                 author='Duane Hilton',
                 author_email='duane9@gmail.com',
                 maintainer='Duane Hilton',
                 url='https://github.com/duane9/printbreakpoint',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 classifiers=CLASSIFIERS,
                 python_requires='>=3.7',
                 keywords=KEYWORDS)
