# $FreeBSD$

PORTNAME=		sane-airscan
DISTVERSION=		0.9.17
CATEGORIES=		graphics

MAINTAINER=		henry.hu.sh@gmail.com
COMMENT=		Scanner Access Now Easy - Apple AirScan (eSCL) driver

LICENSE=		GPLv2
LICENSE_FILE=		${WRKSRC}/LICENSE

LIB_DEPENDS=		libepoll-shim.so:devel/libepoll-shim \
			libavahi-client.so:net/avahi-app \
			libavahi-glib.so:net/avahi-app \
			libjpeg.so:graphics/jpeg-turbo \
			libsoup-2.4.so:devel/libsoup \
			libxml2.so:textproc/libxml2

USES=			gmake
USE_GITHUB=		yes
GH_ACCOUNT=		alexpevzner

MAKE_ARGS=		CC=${CC} MANDIR=${STAGEDIR}${PREFIX}/man PKG_CONFIG=${LOCALBASE}/bin/pkg-config LDFLAGS=-lm CFLAGS=-DLOCALBASE='\"${LOCALBASE}\"' LIBDIR=/lib

MANPAGES=		sane-airscan.5

.include <bsd.port.mk>
