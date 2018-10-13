#! /bin/sh

TG_VER=`make -VDISTVERSION`
LIBTGVOIP_VER=`cat Makefile | grep telegramdesktop:libtgvoip | cut -d : -f 3-3`

(cd $HOME/proj/tdesktop && git diff v$TG_VER..bsd_$TG_VER > patch)
(cd $HOME/proj/libtgvoip && git diff $LIBTGVOIP_VER..HEAD > patch)
rm -f files/patch-* files/gyp-patches
make clean
make extract
cd work/tdesktop-*
patch -p1 < $HOME/proj/tdesktop/patch
cd Telegram/ThirdParty/libtgvoip
patch -p1 < $HOME/proj/libtgvoip/patch
cd ../../../../..
make makepatch
cd files
GYP_FILES=`grep -l %% *`
cat $GYP_FILES > gyp-patches
rm $GYP_FILES
cd ..
make clean
