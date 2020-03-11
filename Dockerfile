# pip install
FROM        python:3.7-slim as python-packages
WORKDIR     /airbnb-clone
COPY        .requirements ./.requirements
RUN         pip install -q -r .requirements/dev.txt

# npm install
FROM        node:12 as node-packages
WORKDIR     /airbnb-clone
COPY        package*.json ./
RUN         npm install

# airbnb-clone
FROM        python:3.7-slim

RUN         apt-get -y -qq update && \
            apt-get -y -qq dist-upgrade && \
            apt-get -y -qq autoremove

# Nginx, gettext, npm 설치
RUN         apt-get -y -qq install nginx && \
            apt-get -y -qq install gettext && \
            apt-get -y -qq install nodejs && \
            apt-get -y -qq install npm && \
            npm install npm@latest -g
RUN         rm -rf /var/lib/apt/lists/* %% \
            apt-get clean

# packages
COPY        --from=node-packages /airbnb-clone/node_modules /srv/airbnb-clone/node_modules
COPY        --from=python-packages /usr/local /usr/local

# 소스코드 복사
COPY        . /srv/airbnb-clone
WORKDIR     /srv/airbnb-clone/app

# Nginx설정파일 링크, 기본 서버 설정 삭제
RUN         rm /etc/nginx/sites-enabled/default
RUN         mv ../.config/airbnb-clone.nginx /etc/nginx/sites-available
RUN         ln /etc/nginx/sites-available/airbnb-clone.nginx /etc/nginx/sites-enabled/airbnb-clone.nginx

# gunicorn 로그폴더 생성
RUN         mkdir /var/log/gunicorn

CMD         /bin/bash
