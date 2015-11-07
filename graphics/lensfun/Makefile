# Created by: Denis Barov <dindin@dindin.ru>
# $FreeBSD: head/graphics/lensfun/Makefile 382801 2015-03-31 08:08:49Z danfe $

PORTNAME=	lensfun
PORTVERSION=	0.3.1
CATEGORIES=	graphics
MASTER_SITES=	SF/${PORTNAME}/${PORTVERSION}

MAINTAINER=	danfe@FreeBSD.org
COMMENT=	Library for fixing lens geometry distortions

LICENSE=	LGPL3

LIB_DEPENDS=	libpng.so:${PORTSDIR}/graphics/png

USES=		cmake pkgconfig zip
USE_GNOME=	glib20
USE_LDCONFIG=	yes
CMAKE_ARGS=	-DINSTALL_HELPER_SCRIPTS:BOOL=OFF

post-patch:
	@${REINPLACE_CMD} -e '/pkgconfig/s,$${LIBDIR},libdata,' \
		${WRKSRC}/libs/lensfun/CMakeLists.txt

.include <bsd.port.mk>
