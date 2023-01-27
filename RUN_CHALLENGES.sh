#!/bin/bash


for file in *
do
    if [ -d $file ]; then
        echo "RUNNNING: $file!!"
        cd $file
        chmod +x TO_RUN.sh
        ./TO_RUN.sh
        cd ..
    fi
done
