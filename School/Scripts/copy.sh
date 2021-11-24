#!/bin/bash
if [[ $1 == "from" ]]
then
    if [ $3 == "to" ]
    then
        cp $2 $4
    fi
    else
        cat $2;
fi    