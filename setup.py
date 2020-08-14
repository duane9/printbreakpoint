import setuptools

LONG_DESCRIPTION = open('README.rst').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'debugging pdb breakpoint print'

setuptools.setup(name='printbreakpoint_duane9',
                 version='0.9.9',
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
