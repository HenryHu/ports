#! /bin/sh

(cd $HOME/proj/tdesktop && git diff v1.3.12..bsd_1.3.12 > patch)
(cd $HOME/proj/libtgvoip && git diff 5380aab..HEAD > patch)
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
