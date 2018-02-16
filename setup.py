#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from setuptools import setup


if sys.version_info < (3, 6):
    print('adaptive requires Python 3.6 or above.')
    sys.exit(1)

install_requires = [
    'scipy',
    'sortedcontainers',
]

extras_require = {
    'recommended': [
        'ipython',
        'ipykernel>=4.8.0',  # because https://github.com/ipython/ipykernel/issues/274 and https://github.com/ipython/ipykernel/issues/263
        'jupyter_client>=5.2.2',  # because https://github.com/jupyter/jupyter_client/pull/314
        'holoviews>=1.9.1',
        'ipyparallel',
        'distributed',
        'ipywidgets',
    ],
}


setup(
    name='adaptive',
    description='Adaptively sample mathematical functions',
    version='0.1a',
    url='https://gitlab.kwant-project.org/qt/adaptive',
    author='Adaptive authors',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['adaptive'],
    install_requires=install_requires,
    extras_require=extras_require,
)
