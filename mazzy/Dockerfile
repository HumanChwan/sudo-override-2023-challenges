FROM frolvlad/alpine-gcc

RUN apk add --no-cache g++
# install tcpserver
RUN apk add ucspi-tcp

# compile the question
COPY mazzy.cpp mazzy.cpp
RUN g++ -o mazzy mazzy.cpp

COPY flag.txt flag.txt
COPY server.sh server.sh

EXPOSE 6868
CMD ["sh", "server.sh"]
