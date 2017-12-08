# Created by: Henry Hu <henry.hu.sh@gmail.com>
# $FreeBSD$

PORTNAME=	telegram-desktop
PORTVERSION=	1.1.23
DISTVERSIONPREFIX=	v
CATEGORIES=	net-im

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	Telegram Desktop messaging app

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	gyp:devel/py-gyp \
		python:lang/python \
		dee-1.0>=0:devel/dee \
		${LOCALBASE}/include/pulse/pulseaudio.h:audio/pulseaudio \
		${LOCALBASE}/include/alsa/asoundlib.h:audio/alsa-lib

LIB_DEPENDS=	libopenal.so:audio/openal-soft \
		libminizip.so:archivers/minizip \
		libavformat.so:multimedia/ffmpeg \
		libopus.so:audio/opus \
		libdbus-1.so:devel/dbus

USE_GITHUB=	yes
GH_ACCOUNT=	telegramdesktop Microsoft:gsl mapbox:variant catchorg:catch
GH_PROJECT=	tdesktop libtgvoip:libtgvoip GSL:gsl variant:variant Catch2:catch
GH_TAGNAME=	v${PORTVERSION} 757a5d8e:libtgvoip c5851a8:gsl 550ac2f:variant 5ca44b68:catch
GH_SUBDIR=	Telegram/ThirdParty/libtgvoip:libtgvoip \
		Telegram/ThirdParty/GSL:gsl \
		Telegram/ThirdParty/variant:variant \
		Telegram/ThirdParty/Catch:catch

USES=		ssl cmake:noninja,outsource gmake pkgconfig
USE_QT5=	buildtools_build core gui widgets network imageformats qmake_build
USE_XORG=	xcb x11
USE_GNOME=	glib20 gtk30

PLIST_FILES=	bin/Telegram

CMAKE_SOURCE_PATH=	${WRKSRC}/out/Release

GYP_DEFINES=	TDESKTOP_DISABLE_CRASH_REPORTS,TDESKTOP_DISABLE_AUTOUPDATE,TDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME

pre-configure:
	cd ${WRKSRC} && gyp \
	    -Dbuild_defines=${GYP_DEFINES} \
	    -Gconfig=Release \
	    --depth=Telegram/gyp --generator-output=../.. -Goutput_dir=out Telegram/gyp/Telegram.gyp --format=cmake
	TOT=`wc -l < ${WRKSRC}/out/Release/CMakeLists.txt` && NUM=`expr $$TOT - 2` && \
	    ${SED} -i -e "$$NUM r ${FILESDIR}/CMakeLists.inj" ${WRKSRC}/out/Release/CMakeLists.txt

do-patch:
	cd ${WRKSRC} && ${SED} -e "s/%%QT_VERSION%%/${QT5_VERSION}/" ${FILESDIR}/patch-tdesktop | ${PATCH} -s -p1
	cd ${WRKSRC}/Telegram/ThirdParty/libtgvoip && ${PATCH} -s -p1 < ${FILESDIR}/patch-libtgvoip

do-install:
	${INSTALL_PROGRAM} ${BUILD_WRKSRC}/Telegram ${STAGEDIR}${PREFIX}/bin

.include <bsd.port.mk>
