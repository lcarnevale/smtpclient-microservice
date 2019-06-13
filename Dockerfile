From alpine:3.7
LABEL maintainer="Lorenzo Carnevale"
LABEL email="lorenzocarnevale@gmail.com"

COPY requirements.txt /opt/app/requirements.txt

# application folder
WORKDIR /opt/app

RUN rm -rf /var/cache/apk/* \
		rm -rf /tmp/*

# update source
RUN apk update && \
		apk add python3 python3-dev && \
		pip3 install --upgrade pip && \
		pip3 install -r requirements.txt && \
		rm -rf /var/cache/apk/* \
		rm -rf /tmp/*


COPY app /opt/app

# copy config files
EXPOSE 5000

CMD ["python3", "app.py"]
