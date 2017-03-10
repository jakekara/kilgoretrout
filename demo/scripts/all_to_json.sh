#!/bin/sh
#
# convert everything in ./clean/csv to ./clean/json
#

for fname in clean/csv/*.csv
do
    bn=$(basename $fname)
    justname=$(echo $bn | cut -f 1 -d '.')
    dst=clean/json/$justname.json
    echo GENERATING $dst
    kilgore -i $fname --json --force > $dst
done
