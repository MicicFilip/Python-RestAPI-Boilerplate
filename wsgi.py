from server import application

if __name__ == '__main__':
  # Flask run instance point
  application.run(port=application.config['PORT'], debug=application.config['DEBUG'])
