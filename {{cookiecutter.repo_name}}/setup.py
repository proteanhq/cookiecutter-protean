#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import absolute_import, print_function

import io, re
from glob import glob
from os.path import basename, dirname, join, splitext

# ThirdParty Library Imports
from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


testing_requires = [
    "flake8-commas==2.0.0",
    "future==0.18.2",
    "mock==4.0.2",
    "pytest-bdd==3.2.1",
    "pytest-cov==2.8.1",
    "pytest-flake8==1.0.4",
    "pytest-flask==0.15.1",
    "pytest-freezegun==0.4.1",
    "pytest-mock==2.0.0",
    "pytest==5.2.1",
]

dev_requires = testing_requires + [
    "bump2version==1.0.0",
]

setup(
    name="{{ cookiecutter.distribution_name }}",
    version="{{ cookiecutter.version }}",
    description={{"{0!r}".format(cookiecutter.project_short_description).lstrip("ub")}},
    long_description="%s\n%s"
    % (
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub(
            "", read("README.rst")
        ),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst")),
    ),
    author={{"{0!r}".format(cookiecutter.full_name).lstrip("ub")}},
    author_email={{"{0!r}".format(cookiecutter.email).lstrip("ub")}},
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=">=3.7",
    install_requires=[
        "protean==0.5.0",
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        "test": testing_requires,
        "tests": testing_requires,
        "testing": testing_requires,
        "dev": dev_requires,
        "all": dev_requires,
    },
)
