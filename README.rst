====================
cookiecutter-protean
====================

Cookiecutter_ template for a Protean Application Repository.
     
.. contents:: Table of Contents

Notes:
-----

This template chooses some project implementations to be available default:

* Pytest_ as the Test Framework
* bumpversion_ for maintaining a semantic version

Requirements
------------

Projects using this template have these dependencies:

* Cookiecutter_ - just for creating the project
* Setuptools_ - for building the package, wheels etc. Setuptools is now packaged by default with most Python Virtual environment managers.

To get quickly started on a new system, just `install setuptools
<https://pypi.org/project/setuptools#installation-instructions>`_ and then `install pip
<https://pip.pypa.io/en/latest/installing.html>`_. That's the bare minimum to required install Cookiecutter_, with this command in your shell or command prompt::

  pip install cookiecutter

Usage and options
-----------------

First generate your project::

  cookiecutter gh:proteanhq/cookiecutter-protean

You will be asked for these fields:

.. list-table::
    :header-rows: 1

    * - Template variable
      - Default
      - Description

    * - ``full_name``
      - .. code:: python

            "Subhash Bhushan C"
      - Main author of this library or application (used in ``setup.py``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``email``
      - .. code:: python

            "subhash.bhushan@gmail.com"
      - Contact email of the author (used in ``setup.py``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``website``
      - .. code:: python

            "https://proteanhq.com"
      - Website of the author.

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``github_username``
      - .. code:: python

            "proteanhq"
      - GitHub user name of this project (used for GitHub link).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``project_name``
      - .. code:: python

            "Domain"
      - Verbose project name, used in headings (docs, readme, etc).

    * - ``repo_name``
      - .. code:: python

            "python-domain"
      - Repository name on GitHub (and project's root directory name).

    * - ``package_name``
      - .. code:: python

            "domain"
      - Python package name (whatever you would import).

    * - ``distribution_name``
      - .. code:: python

            "domain"
      - PyPI distribution name (what you would ``pip install``).

    * - ``project_short_description``
      - .. code:: python

            "An example package [...]"
      - One line description of the project (used in ``README.rst`` and ``setup.py``).

    * - ``version``
      - .. code:: python

            "0.1.0"
      - Release version (see ``.bumpversion.cfg``).

After this you can create the initial repository (make sure you `create <https://github.com/new>`_ an *empty* Github
project)::

  git init .
  git add .
  git commit -m "Initial commit"
  git remote add origin git@github.com:<username>/<repo_name>.git
  git push -u origin master

Developing the project
``````````````````````

To run all the tests, just run::

  pytest

Version management
''''''''''''''''''

This template provides a basic bumpversion_ configuration. It's as simple as running:

* ``bumpversion patch`` to increase version from `1.0.0` to `1.0.1`.
* ``bumpversion minor`` to increase version from `1.0.0` to `1.1.0`.
* ``bumpversion major`` to increase version from `1.0.0` to `2.0.0`.

You should read `Semantic Versioning 2.0.0 <http://semver.org/>`_ before bumping versions.

.. _Setuptools: https://pypi.org/project/setuptools
.. _Pytest: http://pytest.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _bumpversion: https://pypi.org/project/bumpversion
