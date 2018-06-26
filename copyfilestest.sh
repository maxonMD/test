#!/bin/bash

FILE=$1

while read line; do

scp  $user@$line:FILEPATH  LOCATION


done < $FILE

