#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
import sys


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search(
        "^__version__ = ['\"]([^'\"]+)['\"]",
        init_py, re.MULTILINE).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


package = 'dataset_model'
version = get_version(package)


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': version}
    print "You probably want to also tag the version now:"
    print "  git tag -a %(version)s -m 'version %(version)s'" % args
    print "  git push --tags"
    sys.exit()


setup(
    name='dataset-model',
    version=version,
    url='http://github.com/fmartingr/dataset-model',
    license='GPLv2',
    description='Easy model object to work with the dataset framework',
    author='Felipe Martin',
    author_email='fmartingr@me.com',
    keywords='sql sqlalchemy utility dataset',
    packages=get_packages(package),
    package_data=get_package_data(package),
    install_requires=open('requirements.txt').read().split('\n'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
