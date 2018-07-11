# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

install_requires = [
    'numpy',
    'scipy',
    'scikit-learn',
    'sklearn-gbmi',
    'matplotlib',
    'pandas'
]

tests_require = [
    'pytest',
    'sphinx'
]


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='los-ml-tools',
    version='0.1.5',
    description='Library of Logan Martel, ML Developer\'s, personal utilities for ML projects.',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='Logan Martel',
    author_email='logan.martel@outlook.com',
    url='https://github.com/martelogan/los-ml-tools',
    license='GPLv3+',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here.
        'Programming Language :: Python :: 2.7',
    ],
    # What does your project relate to?
    keywords=(
        'Python', 'Machine Learning'
    ),
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='tests'
)
