FROM python:3.5.2

RUN apt-get update && \
    apt-get install -y inotify-tools

# Setup the user
ENV APP_ROOT /home/app/{{ cookiecutter.repo_name }}
WORKDIR $APP_ROOT
ENV APP_USER app
ENV APP_GROUP app
RUN groupadd -r $APP_GROUP && \
    useradd -r -g $APP_USER $APP_GROUP && \
    chown $APP_USER:$APP_GROUP $APP_ROOT && \
    chown -R $APP_USER:$APP_GROUP /usr/local
USER $APP_USER

RUN pip install -U pip setuptools uwsgi

EXPOSE 5000

# Install the requirements
ADD requirements_dev.txt $APP_ROOT/requirements_dev.txt
RUN pip install -r requirements_dev.txt
ADD requirements.txt $APP_ROOT/requirements.txt
RUN pip install -r requirements.txt

ENV PATH $APP_ROOT/image:$PATH
ADD image $APP_ROOT/image

ADD setup.py CONTRIBUTING.rst HISTORY.rst README.rst setup.cfg MANIFEST.in $APP_ROOT/
ADD docs $APP_ROOT/docs

# Required for flask-cli
ENV FLASK_APP $APP_ROOT/{{ cookiecutter.project_slug }}/cli.py

# Add the project files
ADD {{ cookiecutter.project_slug }} $APP_ROOT/{{ cookiecutter.project_slug }}
ADD {{ cookiecutter.project_slug }}_tests $APP_ROOT/{{ cookiecutter.project_slug }}_tests

RUN python setup.py -q install

CMD ["run-app"]
