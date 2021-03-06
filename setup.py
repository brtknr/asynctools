#!/usr/bin/env python
import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = ""
with open('README.md') as f:
    long_description = f.read()

setup(
    name='asynctools',
    version=open(os.path.join('asynctools', 'VERSION')).read().strip(),
    author='Bharat Kunwar',
    author_email='b.kunwar@gmail.com',
    packages=['asynctools', 'asynctools.tests'],
    package_data={'asynctools': [os.path.join('tests', 'urls.txt'), 'VERSION']},
    scripts=['resize_async', 'download_async'],
    url='https://github.com/brtknr/asynctools',
    license='Apache (see LICENSE file)',
    description='Asynchronous tools for Python',
    long_description=long_description,
    python_requires=">=3.5",
    install_requires=[
        'pillow',
        'aiohttp',
        'numpy',
        ],
    test_suite='asynctools.tests'
)
