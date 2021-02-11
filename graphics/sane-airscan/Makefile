# $FreeBSD$

PORTNAME=		sane-airscan
DISTVERSION=		0.99.24
CATEGORIES=		graphics

MAINTAINER=		henry.hu.sh@gmail.com
COMMENT=		Scanner Access Now Easy - Apple AirScan (eSCL) driver

LICENSE=		GPLv2
LICENSE_FILE=		${WRKSRC}/LICENSE

LIB_DEPENDS=		libepoll-shim.so:devel/libepoll-shim \
			libavahi-client.so:net/avahi-app \
			libavahi-glib.so:net/avahi-app \
			libsoup-2.4.so:devel/libsoup \
			libpng16.so:graphics/png \
			libgnutls.so:security/gnutls
BUILD_DEPENDS=		sane-backends>0:graphics/sane-backends

USES=			gettext-runtime gmake jpeg pkgconfig
USE_GNOME=		glib20 libxml2
USE_GITHUB=		yes
GH_ACCOUNT=		alexpevzner

MAKE_ARGS=		CC=${CC} PKG_CONFIG=pkgconf

MANPAGES=		sane-airscan.5 airscan-discover.1

post-install:
	@${MV} ${STAGEDIR}${PREFIX}/etc/sane.d/airscan.conf \
	       ${STAGEDIR}${PREFIX}/etc/sane.d/airscan.conf.sample

.include <bsd.port.mk>
