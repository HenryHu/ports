# Created by: Henry Hu <henry.hu.sh@gmail.com>
# $FreeBSD$

PORTNAME=	tg_owt
PORTVERSION=	0.0.20210207
CATEGORIES=	net-im
MASTER_SITES=	https://chromium.googlesource.com/webm/libvpx.git/+archive/:libvpx \
		https://chromium.googlesource.com/libyuv/libyuv.git/+archive/:libyuv
DISTFILES=	${LIBYUV_TAGNAME}.tar.gz:libvpx \
		${LIBVPX_TAGNAME}.tar.gz:libyuv
EXTRACT_ONLY=	${DISTFILE_DEFAULT}

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	Webrtc library used by telegram-desktop

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	alsa-lib>0:audio/alsa-lib \
		pulseaudio>0:audio/pulseaudio \
		v4l_compat>0:multimedia/v4l_compat \
		yasm:devel/yasm
LIB_DEPENDS=	libavformat.so:multimedia/ffmpeg \
		libjpeg.so:graphics/jpeg-turbo \
		libusrsctp.so:net/libusrsctp \
		libopus.so:audio/opus

USES=		cmake pkgconfig
USE_GITHUB=	yes
GH_ACCOUNT=	desktop-app
GH_PROJECT=	tg_owt
GH_TAGNAME=	a198773

# libvpx version in src/third_party/libvpx/source/libvpx
# libyuv verison in src/third_party/libyuv
LIBYUV_TAGNAME=	ad89006
LIBVPX_TAGNAME=	5b63f0f

# Disable DCHECKs, otherwise video calls will crash.
CXXFLAGS+=	-DNDEBUG

CMAKE_OFF=	BUILD_SHARED_LIBS

post-extract:
	# Extract Git submodules
	(cd ${WRKSRC}/src/third_party/libyuv && \
		${EXTRACT_CMD} ${EXTRACT_BEFORE_ARGS} \
		${_DISTDIR}${LIBYUV_TAGNAME}.tar.gz ${EXTRACT_AFTER_ARGS})
	(cd ${WRKSRC}/src/third_party/libvpx/source/libvpx && \
		${EXTRACT_CMD} ${EXTRACT_BEFORE_ARGS} \
		${_DISTDIR}${LIBVPX_TAGNAME}.tar.gz ${EXTRACT_AFTER_ARGS})

.include <bsd.port.mk>
