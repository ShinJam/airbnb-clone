FROM        python:3.7-slim

RUN         apt-get clean && apt-get -y update && apt-get -y dist-upgrade && apt-get -y autoremove
#RUN         apt -y install nginx

# poetry export로 생성된 requirements.txt를 적절히 복사
COPY        ./requirements.txt /tmp/
RUN         pip install -r /tmp/requirements.txt


# 소스코드 복사
COPY        . /srv/airbnb-clone
WORKDIR     /srv/airbnb-clone/app

# Nginx설정파일을 복사, 기본 서버 설정 삭제
#RUN         rm /etc/nginx/sites-enabled/default
#RUN         cp /srv/instagram/.config/instagram.nginx /etc/nginx/sites-enabled/

# 로그폴더 생성
#RUN         mkdir /var/log/gunicorn

CMD         /bin/bash
