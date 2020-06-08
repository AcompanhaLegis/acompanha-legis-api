#!/usr/local/bin/python

from setuptools import find_packages, setup
from setuptools.command.install import install

setup(
    name='api',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django<3.1',
        'Jinja2<2.12',
        'Markdown<3.3',
        'MarkupSafe<1.2',
        'Pygments<2.7',
        'asgiref<3.3',
        'certifi==2020.4.5.1',
        'chardet<3.1',
        'coreapi<2.4',
        'coreschema<0.1',
        'django-cors-headers<3.4',
        'djangorestframework<3.12',
        'idna<2.10',
        'importlib-metadata<1.7',
        'itypes<1.3',
        'gunicorn<20.1',
        'psycopg2',
        'pytz==2020.1',
        'requests<2.24',
        'sqlparse<0.4',
        'uritemplate<3.1',
        'urllib3<1.26',
        'zipp<3.2',

    ],
    entry_points={
        'console_scripts': [
            'api=manage:main',
        ],
    },
    scripts=['manage.py'],
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=[],
    license='No license',
)
