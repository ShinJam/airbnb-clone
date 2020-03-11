# npm install
FROM        node:12 as node-packages
WORKDIR     /airbnb-clone
COPY        ./app/assets/scss/ ./app/assets/scss
COPY        package*.json ./
COPY        ./gulpfile.js ./
RUN         npm install -q
RUN         mkdir -p static/css
RUN         npm run css

# airbnb-clone
FROM        python:3.7-slim

RUN         apt-get -y -qq update && \
            apt-get -y -qq dist-upgrade && \
            apt-get -y -qq autoremove

# Nginx, gettext, npm 설치
RUN         apt-get -y -qq install nginx && \
            apt-get -y -qq install gettext && \
            rm -rf /var/lib/apt/lists/* && \
            apt-get clean

# packages
COPY        --from=node-packages /airbnb-clone/node_modules /srv/airbnb-clone/node_modules
COPY        --from=node-packages /airbnb-clone/static/css /srv/airbnb-clone/static/css
COPY        ./.requirements /srv/airbnb-clone/.requirements
RUN         pip install -q -r /srv/airbnb-clone/.requirements/dev.txt

# 소스코드 복사
COPY        ./app /srv/airbnb-clone/app
WORKDIR     /srv/airbnb-clone/app

# 언어 설정 복사
COPY        ./locale/ko/LC_MESSAGES/django.po ../locale/ko/LC_MESSAGES/

# media 복사
COPY        ./uploads ../uploads
COPY        ./static/img    ../static/img

# config 파일 복사(nginx, gunicorn, supervisor)
COPY        ./.config ../.config

# Nginx설정파일 링크, 기본 서버 설정 삭제
RUN         rm /etc/nginx/sites-enabled/default
COPY        ./.config/airbnb-clone.nginx /etc/nginx/sites-available
RUN         ln /etc/nginx/sites-available/airbnb-clone.nginx /etc/nginx/sites-enabled/airbnb-clone.nginx

# gunicorn 로그폴더 생성
RUN         mkdir /var/log/gunicorn

CMD         /bin/bash
