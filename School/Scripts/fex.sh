#!/bin/bash
FILE=$1
if [ -f "$FILE" ]
then
	ls -l $FILE
	cat $FILE
fi
