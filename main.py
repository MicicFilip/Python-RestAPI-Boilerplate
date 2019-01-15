from server import application

if __name__ == '__main__':
  # Flask run instance point
  application.run(host=application.config['HOST'], port=application.config['PORT'],
    debug=application.config['DEBUG'])
