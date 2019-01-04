#!/bin/bash

# Load config variables
source config.sh

SIZE=1200x900
OUTPUT_DIR=${IMAGES_DIR}_${SIZE}

# For each output image
mkdir -p ${OUTPUT_DIR}
for item in $(ls ${IMAGES_DIR})
do
    echo $item
    convert ${IMAGES_DIR}/${item} -resize ${SIZE} ${OUTPUT_DIR}/${item}
done