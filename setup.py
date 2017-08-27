#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(eyalev): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
]

setup(
    name='hello_world_python',
    version='0.1.0',
    description="hello-world-python",
    long_description=readme + '\n\n' + history,
    author="Eyal Levin",
    author_email='eyalev@gmail.com',
    url='https://github.com/eyalev/hello_world_python',
    packages=find_packages(include=['hello_world_python']),
    entry_points={
        'console_scripts': [
            'hello-world-python=hello_world_python.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='hello_world_python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
