#!/usr/local/bin/python

from setuptools import find_packages, setup
from setuptools.command.install import install

setup(
    name='acompanha_legis',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests<2.24'
    ],
    entry_points={
        'console_scripts': [
            'acompanha_legis=acompanha_legis.__main__:main',
        ],
    },
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=[],
    license='No license',
)
