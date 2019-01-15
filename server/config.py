class Config(object):
  """
  Global configuration object
  """
  # Flask web server configuration
  HOST = '127.0.0.1'
  PORT = 3000

  # Debug mode should never be used in production
  # because it allows the execution of arbitrary code
  DEBUG = True

class TestConfig(object):
  """
  Testing configuration object
  """
  pass