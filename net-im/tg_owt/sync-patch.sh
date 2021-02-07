#! /bin/sh

TG_VER=2.5.8
# latest version of tg_owt
OWT_VER=`make -V GH_TAGNAME`

MY_VER=bsd_$TG_VER

(cd $HOME/proj/tg_owt && git diff $OWT_VER $MY_VER > patch)
rm -f files/patch-*
make clean
make extract
cd work/tg_owt-*
patch -p1 < $HOME/proj/tg_owt/patch
cd ../..
make makepatch
make clean
