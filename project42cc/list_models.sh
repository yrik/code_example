#!/bin/bash

filename=`date "+%m-%d-%y"`.dat
echo $filename
python manage.py statistic 2>$filename  
