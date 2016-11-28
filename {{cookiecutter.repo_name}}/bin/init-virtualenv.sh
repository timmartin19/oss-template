#!/usr/bin/env bash -evx

mkvirtualenv "{{ cookiecutter.repo_name }}"
workon "{{ cookiecutter.repo_name }}"

pip install -e .
pip install -r requirements_dev.txt
