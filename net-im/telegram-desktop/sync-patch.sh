#! /bin/sh

TG_VER=`make -VDISTVERSION`
LIBTGVOIP_VER=522550a1

(cd $HOME/proj/tdesktop && git diff v$TG_VER..bsd_$TG_VER > patch)
(cd $HOME/proj/libtgvoip && git diff $LIBTGVOIP_VER..HEAD > patch)
(cd $HOME/proj/lib_ui && git diff upstream/master master > patch)
(cd $HOME/proj/lib_base && git diff upstream/master master > patch)
(cd $HOME/proj/cmake_helpers && git diff upstream/master master > patch)
rm -f files/patch-*
make clean
make extract
cd work/tdesktop-*
patch -p1 < $HOME/proj/tdesktop/patch
(cd Telegram/ThirdParty/libtgvoip && patch -p1 < $HOME/proj/libtgvoip/patch)
(cd Telegram/lib_ui && patch -p1 < $HOME/proj/lib_ui/patch)
(cd Telegram/lib_base && patch -p1 < $HOME/proj/lib_base/patch)
(cd cmake && patch -p1 < $HOME/proj/cmake_helpers/patch)
cd ../..
make makepatch
make clean
