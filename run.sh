#!/bin/bash

if [ $# -ne 2 ]; then
    echo "run.sh [image_dir] [gray | laplacian | sobelx | sobely | canny]"
    exit 1
fi

# Load config
source config.sh

IMAGES_DIR=$1
PROCESS=$2
OUTPUT_FILE=${IMAGES_DIR}_${PROCESS}.csv


# Remove existing dataset
rm ${OUTPUT_FILE}

# For each image
for item in `ls ${IMAGES_DIR}`;
do
    echo "Exec: image_to_array.py" ${IMAGES_DIR}/${item} ${PROCESS}
    ./image_to_array.py ${IMAGES_DIR}/${item} ${PROCESS} >> ${OUTPUT_FILE};
done;