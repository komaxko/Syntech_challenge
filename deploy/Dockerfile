FROM python:3.7-stretch as builder

ADD ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

ARG python_version=3.7
ARG user_name=app_user
ARG user_home=/home
ARG app_dir=${user_home}/app

COPY . / ${app_dir}/
WORKDIR ${app_dir}

USER root
RUN chmod +x scripts/post.sh

RUN useradd -Ms /bin/bash ${user_name} \
    && chown -R ${user_name} ${user_home}

USER ${user_name}
WORKDIR ${app_dir}

EXPOSE 8000
