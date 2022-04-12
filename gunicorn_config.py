"""Gunicorn *development* config file"""

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "zwb_lucky.wsgi:application"
# The granularity of Error log outputs
loglevel = "info"
# The number of worker processes for handling requests
workers = 2
# The socket to bind
bind = "0.0.0.0:8000"
# Restart workers when code changes (development only!)
reload = False
# Write access and error info to /var/log
accesslog = "/webroot/logs/app.log"
errorlog  = "/webroot/logs/error.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/webroot/run/gunicorn.pid"