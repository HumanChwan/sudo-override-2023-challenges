#!/bin/bash

t=$(cat super_passwd.txt)

for i in {1..250} 
do
    t=$(echo $t | base64 -di | zcat)
done

echo $t
