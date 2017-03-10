#!/bin/sh
#
# Make master schools list
# source: raw/findSchoolDistrict.csv
# dest: clean/csv/schools.csv
#

SRC=raw/findSchoolDistrict.csv
DST=clean/csv/schools.csv
JSDST=clean/json/schools.json

# Make clean spreadsheet
scripts/forceutf8.sh $SRC | kilgore --skiprows=1 --pretty\
			       --colnames="type","district","school_code","school","street","city","state","zip","phone","fax","website","education_program","program_type","inter_district_magnet","pre_kindergarten","kindergarten","grade_1","grade_2","grade_3","grade_4","grade_5","grade_6","grade_7","grade_8","grade_9","grade_10","grade_11","grade_12"\
			       --load rmequals\
                               --load adddist > $DST

