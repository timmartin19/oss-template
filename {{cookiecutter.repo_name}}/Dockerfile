FROM python:alpine

RUN apk add --no-cache inotify-tools bash gcc musl-dev linux-headers libxslt-dev libffi-dev postgresql-dev

# Setup the user
ENV USER_ROOT="/home/app" \
    APP_ROOT="/home/app/{{ cookiecutter.repo_name }}" \
    APP_USER="app" \
    APP_GROUP="app"
WORKDIR $APP_ROOT
RUN addgroup $APP_GROUP && \
    adduser -h $USER_ROOT -D -G $APP_USER $APP_GROUP && \
    chown -R $APP_USER:$APP_GROUP $USER_ROOT && \
    chown -R $APP_USER:$APP_GROUP /usr/local
USER $APP_USER

RUN pip install -U pip setuptools uwsgi

EXPOSE 5000

# Install the requirements
ADD requirements.txt $APP_ROOT/requirements.txt
RUN pip install -r requirements.txt

ENV PATH="$APP_ROOT/image:$PATH" \
    FLASK_APP="$APP_ROOT/{{ cookiecutter.project_slug }}/cli.py"

ADD image $APP_ROOT/image
CMD ["run-app"]

ADD setup.py CONTRIBUTING.rst HISTORY.rst README.rst setup.cfg MANIFEST.in $APP_ROOT/
ADD docs $APP_ROOT/docs

# Add the project files
ADD {{ cookiecutter.project_slug }} $APP_ROOT/{{ cookiecutter.project_slug }}
ADD {{ cookiecutter.project_slug }}_tests $APP_ROOT/{{ cookiecutter.project_slug }}_tests
