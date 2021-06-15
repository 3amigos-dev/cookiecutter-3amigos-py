FROM python:3.9-slim
COPY install.sh /build/install.sh
COPY pip /build/pip
RUN /build/install.sh
WORKDIR /workspace/cookiecutter
ENV HOME /workspace/cookiecutter
