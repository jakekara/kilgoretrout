#!/bin/sh
#
# Run all scripts
#

echo GENERATING MASTER SCHOOLS LIST
echo ==============================
scripts/master_schools_list.sh

echo
echo GENEREATING ABSENTEEISM SHEETS
echo ==============================
scripts/absenteeism.sh

echo
echo CONVERTING ALL CSV FILES TO JSON
echo ================================
scripts/all_to_json.sh

