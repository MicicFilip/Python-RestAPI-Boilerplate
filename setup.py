from setuptools import setup, find_packages

setup(
  name='python-flask-boilerplate',
  version='0.1.0',
  url='https://github.com/MicicFilip/Python-RestAPI-Boilerplate',
  description="""Python Flask Boilerplate""",
  packages=find_packages(),
  author=['Filip Micic'],
  author_email=['micic.filip@protonmail.com'],
  install_requires=[
        'Flask>=0.12',
        'gunicorn>=19.0.1'
    ],
)