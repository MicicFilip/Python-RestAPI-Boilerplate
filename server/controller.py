from flask import request
from server import application

@application.route('/', methods = ['GET'])
def home_endpoint():
  return 'Python WebAPI Boilerplate', 200
