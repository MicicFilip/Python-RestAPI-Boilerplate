from server.core.app_entry import api_v1
from server.core.database import users
from server.api.utils import senseless_print

from flask import jsonify

# Simple example of a rest route 
@api_v1.route('/users', methods = ['GET'])
def route_users():
  users_data = []
  for user in users:
    user_data = {
      'name': user.name,
      'email': user.email
    }
    users_data.append(user_data)
  
  senseless_print()
  return jsonify(users_data), 200