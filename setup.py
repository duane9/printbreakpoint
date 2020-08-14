import setuptools

VERSION = '0.9.9'

LONG_DESCRIPTION = open('README.rst').read()

CLASSIFIERS = [
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.8',
]

KEYWORDS = 'debugging pdb breakpoint print'

setuptools.setup(name='printbreakpoint_duane9',
                 version=VERSION,
                 description='Print breakpoint',
                 long_description=LONG_DESCRIPTION,
                 author='Duane Hilton',
                 author_email='duane9@gmail.com',
                 maintainer='Duane Hilton',
                 download_url='https://test.pypi.org/project/pd-duane9/0.9/',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 classifiers=CLASSIFIERS,
                 python_requires='>=3.7',
                 keywords=KEYWORDS)
