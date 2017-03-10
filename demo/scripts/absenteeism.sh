#!/bin/sh
#
# Make absenteeism csv
#
# Requires file:
# chronic_absenteeism_ell.csv
# chronic_absenteeism_frpl.csv
# chronic_absenteeism_gender.csv
# chronic_absenteeism_grade.csv
# chronic_absenteeism_race_ethnicity.csv
# chronic_absenteeism_special_ed.csv
#

clean_abs()
{
    echo "cleaning $1"
    bn=$(basename $1)
    justname=$(echo $bn | cut -f 1 -d '.')

    kilgore --skiprows 4 -i $1 --pretty\
       --load clean_code_columns > clean/csv/$justname.csv
}

for fname in raw/*_absenteeism_*.csv
do
    clean_abs $fname
done

