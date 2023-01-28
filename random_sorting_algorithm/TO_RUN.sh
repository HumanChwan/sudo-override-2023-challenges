#!/bin/bash

function exit_code () {
    if [ $? -ne 0 ];
    then
        echo "poo poo: at $1"
    fi
}

docker stop `docker ps -a | grep 'random_sorting_algorithm' | head -n 1 | rev | cut -d ' ' -f1 | rev`
exit_code "removing ps"

docker rmi -f random_sorting_algorithm
exit_code "removing image"

docker build -t random_sorting_algorithm .
exit_code "build"

# TODO: decide the port (keeping it 6553 for now)
docker run -d -p 6553:6553 random_sorting_algorithm
exit_code "run"
