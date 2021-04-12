""" SMTP Client Mime Type Wrapper
.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019-2020, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'

#standard libraries
from email.message import EmailMessage

def mime_email(from_, to, subject, body):
    """
    Args:
        images (list): list of binaries
    """
    msg = EmailMessage()

    # generic email headers
    msg['Subject'] = subject
    msg['From'] = from_
    msg['To'] = to

    # setting plain text body
    msg.set_content(body)

    return msg
