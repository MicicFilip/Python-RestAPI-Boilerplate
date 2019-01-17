import logging
import os

from flask import Flask
from logging import Formatter

#############################################
#             Web Server                    #
#############################################
# This is how we initialize a Flask application
application = Flask(__name__)

# Global settings variables are inside config.py
application.config.from_object('server.config.Config')

#############################################
#               Logging                     #
#############################################

# Create a log file handler
log_handler = logging.FileHandler('python-server.log')

log_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))

# Default level is INFO in production and DEBUG in debug mode
if application.debug:
    log_handler.setLevel(logging.DEBUG)
else:
    log_handler.setLevel(logging.INFO)

application.logger.addHandler(log_handler)

# Controllers are the main entry points
# of our app so we have to load them here
import server.controller