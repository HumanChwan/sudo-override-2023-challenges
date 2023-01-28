FROM alpine:latest

# intalling tcpserver
RUN apk add ucspi-tcp

# installing python
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# installing Crypto package
RUN pip3 install pycryptodome

COPY rsa.py rsa.py

EXPOSE 6553
CMD ["tcpserver", "0.0.0.0", "6553", "./rsa.py"]
