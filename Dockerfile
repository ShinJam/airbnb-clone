FROM        python:3.7-slim

RUN         apt-get clean && \
            apt-get -y -qq update && \
            apt-get -y -qq dist-upgrade && \
            apt-get -y -qq autoremove

# Nginx, gettext, npm 설치
RUN         apt-get -y -qq install nginx
RUN         apt-get -y -qq install gettext
RUN         apt-get -y -qq install nodejs
RUN         apt-get -y -qq install npm
RUN         npm install npm@latest -g

# 소스코드 복사
COPY        . /srv/airbnb-clone
WORKDIR     /srv/airbnb-clone/app

# requirements.txt(dev)
RUN         pip install -r ../.requirements/dev.txt

# Nginx설정파일 링크, 기본 서버 설정 삭제
#RUN         rm /etc/nginx/sites-enabled/default
RUN         mv .config/airbnb-clone.conf /etc/nginx/sites-available
RUN         ln /etc/nginx/sites-available/airbnb-clone/airbnb-clone.conf /etc/nginx/sites-enabled/airbnb-clone.conf

# gunicorn 로그폴더 생성
RUN         mkdir /var/log/gunicorn

CMD         /bin/bash
