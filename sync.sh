#! /bin/sh
#
# sync.sh
# Copyright (C) 2018 henryhu <henryhu@goldpeak>
#
# Distributed under terms of the BSD license.
#


for makefile in `find . -name Makefile -depth 3`; do
    portdir=`dirname $makefile`
    catname=`echo $portdir | cut -d / -f 2-2`
    portname=`echo $portdir | cut -d / -f 3-3`
    fullname="$catname/$portname"

    if [ ! -d /usr/ports/$fullname ]; then
        echo "$fullname has been removed from the ports tree."
        continue
    fi

    diff_ret=`diff -x work -x '*.orig' /usr/ports/$fullname $portdir`
    if [ $? = 0 ]; then
        #echo "$fullname has no diff"
        continue
    fi

    echo "=== $fullname has diff ==="
    portver=`cd /usr/ports/$fullname; make -V PORTVERSION`
    repover=`cd $portdir; make -V PORTVERSION`
    echo "Port tree version: $portver Repo version: $repover"
    compare=`pkg version -t $portver $repover`
    if [ "$compare" = "<" ]; then
        echo "Repo version is newer. Skip sync."
        continue
    fi
    if [ "$compare" = "=" ]; then
        echo "Same version. Skip."
        continue
    fi
    if [ "$compare" = ">" ]; then
        echo "Port is newer than repo. Update."
    fi

    diff -ruN -x work -x '*.orig' $portdir /usr/ports/$fullname
    read -e -p "Sync $fullname with the port version? " answer
    [ $answer == "y" -o $answer == "Y" ] && cp -r /usr/ports/$fullname/* $portdir/ && git add -p $portdir
    if [ -d $portdir/files ]; then
        git add $portdir/files
    fi
done
