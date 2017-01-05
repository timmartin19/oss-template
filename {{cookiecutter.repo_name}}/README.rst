{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
===============================
{{ cookiecutter.project_name }}
===============================

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Documentation
-------------

You will need to install the package dependencies first,
see the Installation section for details.

To build and open the documentation simply run:

.. code-block:: bash

    bin/build-docs

Installation
------------

If you need to install pyenv/virtualenvwrapper you can run the ``bin/setup-osx`` command
Please note that this will modify your bash profile

Assuming you have virtualenv wrapper installed

.. code-block:: bash

    mkvirtualenv {{ cookiecutter.repo_name }}
    workon {{ cookiecutter.repo_name }}
    pip install -r requirements_dev.txt
    pip install -e .

Docker
""""""

If you want to use docker for this project

1. Download and install `Docker for Mac <https://docs.docker.com/docker-for-mac/>`_
2. In the root of this repo: ``docker-compose build``
3. ``docker-compose up``
4. Verify the application is running with: ``curl http://localhost:5000/status``

PyCharm
"""""""

To integrate PyCharm with your virtual environment

1. install according to the standard installation instructions
2. In your project settings (shortcut: ``cmd+,``) navigate to ``Project -> Project Interpreter``
3. Select the gear icon in the upper right corner
4. Select ``Add Local``
5. Select ``$HOME/.envs/{{ cookiecutter.repo_name }}/bin/python3.5`` and click ``OK``
6. Click ``Apply`` and then ``OK``

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `timmartin19/oss-template@flask`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _timmartin19/oss-template@flask: https://github.com/timmartin19/oss-template/tree/flask

