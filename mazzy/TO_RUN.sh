#!/bin/bash

function exit_code () {
    if [ $? -ne 0 ];
    then
        echo "poo poo: at $1"
    fi
}

docker stop `docker ps -a | grep 'mazzy' | head -n 1 | rev | cut -d ' ' -f1 | rev`
exit_code "removing ps"

docker rmi -f mazzy
exit_code "removing image"

docker build -t mazzy .
exit_code "build"

# TODO: decide the port (keeping it 4545 for now)
docker run -d -p 4545:22 mazzy
exit_code "run"
