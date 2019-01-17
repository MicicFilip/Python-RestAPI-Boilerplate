class Config(object):
  """
  Global configuration object
  """
  # Flask web server configuration
  HOST = '127.0.0.1'
  PORT = {{ app_port }}

  # Debug mode should never be used in production
  # because it allows the execution of arbitrary code
  DEBUG = {{ app_debug }}

class TestConfig(object):
  """
  Testing configuration object
  """
  pass