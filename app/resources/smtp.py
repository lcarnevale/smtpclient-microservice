""" SMTP Client Resources Collection
.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019-2020, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'

# standard libraries
import yaml
import smtplib
# local libraries
from common.mimeemail import mime_email
# third parties libraries
from flask import request
from flask_restful import Resource


class SMTPGmailClient(Resource):
    """ Gmail SMTP Client

    Args:
        __username (str): Gmail account;
        __password (str): Gmail account's password;
        __sent_from (str): mail's sender.
    """
    def __init__(self):
        """ Constructor
        """
        with open('conf.yaml', 'r') as f:
            conffile = yaml.load(f, Loader=yaml.Loader)

        # smtp credentials
        self.__username = conffile['username']
        self.__password = conffile['password']
        # mail settings
        self.__sent_from = conffile['sent_from']


    def __create_email(self):
        """ Sets up mail metadata
        """
        json_data = request.get_json(force=True)

        sent_from = self.__sent_from
        to = json_data["to"]
        subject = json_data["subject"]
        body = json_data["body"]

        return sent_from, to, subject, body

    def post(self):
        """ HTTP POST request to send a mail
        """
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        
        server.login(self.__username, self.__password)

        sent_from, to, subject, email_text = self.__create_email()
        msg = mime_email(sent_from, to, subject, email_text)

        server.send_message(msg)
        server.close()
