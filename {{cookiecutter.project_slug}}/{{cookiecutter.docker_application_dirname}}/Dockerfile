FROM 3amigos/pipenv-all:latest
ENV PYTHONVERS "{% if cookiecutter.supports_pytwo == 'yes' %}2.7 {% endif %}3.5 3.6 3.7 3.8"
COPY install.sh /build/install.sh
COPY pip /build/pip
RUN /build/install.sh
WORKDIR /{{ cookiecutter.docker_workspace_dirname }}/{{ cookiecutter.docker_application_dirname }}
ENV HOME /{{ cookiecutter.docker_workspace_dirname }}/{{ cookiecutter.docker_application_dirname }}
