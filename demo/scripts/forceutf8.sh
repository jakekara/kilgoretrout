#!/bin/sh
#
# force utf-8 characters, dropping offenders
#

iconv -f utf-8 -t utf-8 -c $1 
