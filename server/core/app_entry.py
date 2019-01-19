from flask import request, jsonify, Blueprint
# This line has to be here, otherwise we will get import error
api_v1 = Blueprint('api_v1', __name__)

# Import rest of the endpoints
from server.api import api

@api_v1.route('/', methods = ['GET'])
def home_endpoint():
  return jsonify({'message': 'Python WebAPI Boilerplate'}), 200