#!/usr/bin/env python3
#
#
#

from setuptools import find_packages, setup


setup(
    name='elib_django',
    use_scm_version=True,
    license='Apache-2.0',

    description='elib_django',
    long_description='elib_django',
    url='https://github.com/east301/elib_django.git',

    author='east301',
    author_email='me@east301.net',

    keywords='django',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP'
    ],

    packages=find_packages()
)
