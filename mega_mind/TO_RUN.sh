#!/bin/bash

function exit_code () {
    if [ $? -ne 0 ];
    then
        echo "poo poo: at $1"
    fi
}

docker stop `docker ps -a | grep 'mega_mind' | head -n 1 | rev | cut -d ' ' -f1 | rev`
exit_code "removing ps"

docker rmi -f mega_mind
exit_code "removing image"

docker build -t mega_mind .
exit_code "build"

# TODO: decide the port (keeping it 3141 for now)
docker run -d -p 3141:3141 mega_mind
exit_code "run"
