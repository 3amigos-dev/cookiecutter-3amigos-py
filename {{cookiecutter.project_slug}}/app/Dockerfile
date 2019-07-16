FROM 3amigos/pipenv-all:latest
COPY install.sh /build/install.sh
COPY pip /build/pip
RUN /build/install.sh
WORKDIR /{{ cookiecutter.docker_workspace_dirname }}/{{ cookiecutter.docker_application_dirname }}
ENV HOME /{{ cookiecutter.docker_workspace_dirname }}/{{ cookiecutter.docker_application_dirname }}
