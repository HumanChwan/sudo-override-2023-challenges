wsgi_app = 'susBlog.wsgi'
bind = '0.0.0.0:8000'
workers = 4
loglevel = "debug"
threads = 4
pid = './conf/gunicorn.pid'
