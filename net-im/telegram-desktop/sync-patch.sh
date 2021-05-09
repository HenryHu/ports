#! /bin/sh

TG_VER=`make -VDISTVERSION`
# version of Telegram/ThirdParty/libtgvoip submodule.
LIBTGVOIP_VER=13a5fcb
# version of cmake submodule.
CMAKE_VER=52ccf5e
# latest version of tg_owt
# OWT_VER=`cat Makefile | grep desktop-app:tg_owt | cut -d : -f 3-3 `
LIBBASE_VER=356daf5

MY_VER=bsd_$TG_VER

(cd $HOME/proj/tdesktop && git diff v$TG_VER..$MY_VER > patch)
(cd $HOME/proj/libtgvoip && git diff $LIBTGVOIP_VER..HEAD > patch)
(cd $HOME/proj/lib_ui && git diff upstream/master master > patch)
(cd $HOME/proj/lib_base && git diff $LIBBASE_VER $TG_VER > patch)
(cd $HOME/proj/cmake_helpers && git diff $CMAKE_VER $MY_VER > patch)
#(cd $HOME/proj/tg_owt && git diff $OWT_VER $MY_VER > patch)
rm -f files/patch-*
make clean
make extract
cd work/tdesktop-*
echo '######### Applying patch for tdesktop #########'
patch -p1 < $HOME/proj/tdesktop/patch
echo '######### Applying patch for tgvoip #########'
(cd Telegram/ThirdParty/libtgvoip && patch -p1 < $HOME/proj/libtgvoip/patch)
echo '######### Applying patch for lib_ui #########'
(cd Telegram/lib_ui && patch -p1 < $HOME/proj/lib_ui/patch)
echo '######### Applying patch for lib_base #########'
(cd Telegram/lib_base && patch -p1 < $HOME/proj/lib_base/patch)
echo '######### Applying patch for cmake_helpers #########'
(cd cmake && patch -p1 < $HOME/proj/cmake_helpers/patch)
#(cd tg_owt && patch -p1 < $HOME/proj/tg_owt/patch)
rm Telegram/ThirdParty/hunspell/tests/suggestiontest/Makefile.orig
cd ../..
make makepatch
make clean
