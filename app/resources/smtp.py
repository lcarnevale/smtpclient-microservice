# standard libraries
import yaml
import smtplib
# third parties libraries
from flask import request
from flask_restful import Resource


class SMTPGmailServer(Resource):
    """
    """
    def __init__(self):
        """
        """
        with open('conf.yaml', 'r') as f:
            conffile = yaml.load(f, Loader=yaml.Loader)

        # smtp credentials
        self.__username = conffile['username']
        self.__password = conffile['password']
        # mail settings
        self.__sent_from = conffile['sent_from']


    def __create_email(self):
        """
        """
        json_data = request.get_json(force=True)

        sent_from = self.__sent_from
        to = json_data["to"]
        subject = json_data["subject"]
        body = json_data["body"]

        return sent_from, to, body

    def post(self):
        """
        """
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        # server.ehlo()
        server.login(self.__username, self.__password)

        sent_from, to, email_text = self.__create_email()
        server.sendmail(sent_from, to, email_text)

        server.close()
