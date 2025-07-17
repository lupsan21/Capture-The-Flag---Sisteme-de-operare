#!/bin/bash

files=40
for i in $(seq -w 1 $files); do
    head -c 32 /dev/urandom > "file${i}.bin"
done

