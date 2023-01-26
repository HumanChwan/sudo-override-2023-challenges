#!/bin/bash

t=$(cat passwd.txt)

for i in {1..250}
do
    echo -n "$i "
    t=$(echo $t | gzip | base64)
done

echo $t > super_passwd.txt

