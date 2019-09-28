# SMTP Client Microservice
![Alt text](./docs/shields/python-3.6-blue.svg)

A Python Flask implementation of a SMTP Client Microservice. It uses Gmail to send mails out through a HTTP POST request.

This project is part of the scientific research made up at [University of Messina](https://www.unime.it/en) and it aims to be a research product.

## Microservice

### How to run it
Modify the configuration file first
```yaml
username: YOUR_GMAIL_ACCOUNT
password: YOUR_APPLICATION_PASSWORD

sent_from: SENDER_MAIL_ADDRESS
```

Build an image using the Dockerfile:
```bash
$ docker build -t lcarnevale/smtpclient-microservice .
```

Run the image, exposing the dev port:
```bash
$ docker run -d --rm -p 5000:5000 --name smtpclient-microservice lcarnevale/smtpclient-microservice
```

### How to use it
Try to send a mail out with a curl:
```bash
$ curl -d '{ \
  "to":["RECIPIENT_MAIL_ADDRESS"], \
  "subject":"Test SMTP Client Microservice", \
  "body":"This mail is sent out by the SMTP Client Microservice.\n\nLorenzo" \
}' \
-H "Content-Type: application/json" \
-X POST http://localhost:5000/
```

## Credits
Inspired by a [Scott Robinson](https://twitter.com/ScottWRobinson) [post](https://stackabuse.com/how-to-send-emails-with-gmail-using-python/).
