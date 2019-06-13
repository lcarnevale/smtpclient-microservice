""" Web Application

.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'

# third parties libraries
from flask import Flask
from flask_restful import Api
from resources.smtp import SMTPGmailClient

app = Flask(__name__)
api = Api(app)

api.add_resource(SMTPGmailClient, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
