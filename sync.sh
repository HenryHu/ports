#! /bin/sh
#
# sync.sh
# Copyright (C) 2018 henryhu <henryhu@goldpeak>
#
# Distributed under terms of the MIT license.
#


for makefile in `find . -name Makefile -depth 3`; do
    portdir=`dirname $makefile`
    catname=`echo $portdir | cut -d / -f 2-2`
    portname=`echo $portdir | cut -d / -f 3-3`
    fullname="$catname/$portname"

    diff_ret=`diff -x work -x '*.orig' /usr/ports/$fullname $portdir`
    if [ $? = 0 ]; then
        echo "$fullname has no diff"
        continue
    fi

    echo "$fullname has diff!"
    diff -ruN -x work -x '*.orig' /usr/ports/$fullname $portdir

    read -e -p "Sync $fullname with the port version? " answer
    [ $answer == "y" -o $answer == "Y" ] && cp -r /usr/ports/$fullname/* $portdir/; git add -p $portdir
done
