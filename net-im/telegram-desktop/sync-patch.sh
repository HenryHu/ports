#! /bin/sh

TG_VER=1.3.14
LIBTGVOIP_VER=bfa1e6a

(cd $HOME/proj/tdesktop && git diff v$TG_VER..bsd_$TG_VER > patch)
(cd $HOME/proj/libtgvoip && git diff bfa1e6a..HEAD > patch)
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
