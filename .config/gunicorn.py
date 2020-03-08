daemon = False
chdir = '/srv/airbnb-clone/app'
bind = 'unix:/run/airbnb-clone.sock'
accesslog = '/var/log/gunicorn/airbnb-clone-access.log'
errorlog = '/var/log/gunicorn/airbnb-clone-error.log'
capture_output = True
