# Created by: Henry Hu <henry.hu.sh@gmail.com>
# $FreeBSD$

PORTNAME=	tg_owt
PORTVERSION=	0.0.20201025
CATEGORIES=	net-im

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	Webrtc library used by telegram-desktop

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	alsa-lib>0:audio/alsa-lib \
		pulseaudio>0:audio/pulseaudio

LIB_DEPENDS=	libavformat.so:multimedia/ffmpeg \
		libjpeg.so:graphics/jpeg-turbo

USES=		cmake pkgconfig
USE_GITHUB=	yes
GH_ACCOUNT=	desktop-app
GH_PROJECT=	tg_owt
GH_TAGNAME=	c73a471

do-install:
	@${INSTALL_DATA} ${BUILD_WRKSRC}/libtg_owt.a ${STAGEDIR}${PREFIX}/lib
	@${MKDIR} ${STAGEDIR}${PREFIX}/lib/cmake/tg_owt
	@${INSTALL_DATA} ${BUILD_WRKSRC}/tg_owtConfig.cmake ${STAGEDIR}${PREFIX}/lib/cmake/tg_owt
	@${INSTALL_DATA} ${BUILD_WRKSRC}/tg_owtTargets.cmake ${STAGEDIR}${PREFIX}/lib/cmake/tg_owt

.include <bsd.port.mk>
