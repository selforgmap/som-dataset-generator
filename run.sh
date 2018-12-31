#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: generate.sh <directory_to_images>"
    exit 1
fi

# Remove existing dataset
rm dataset.csv

# For each image
for i in $(ls $1);
do echo Loading $i; ./image_to_array.py $1/$i >> dataset.csv;
done;