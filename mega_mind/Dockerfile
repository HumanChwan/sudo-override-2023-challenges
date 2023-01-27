FROM frolvlad/alpine-gcc

RUN apk add --no-cache g++
# install tcpserver
RUN apk add ucspi-tcp

# compile the question
COPY mega_mind.cpp mega_mind.cpp
RUN g++ -o mega_mind mega_mind.cpp

COPY flag.txt flag.txt
COPY payload.py payload.py
COPY server.sh server.sh

EXPOSE 3141
CMD ["sh", "server.sh"]
