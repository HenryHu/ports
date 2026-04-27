# Created by: Henry Hu <henry.hu.sh@gmail.com>

PORTNAME=	nvtop
PORTVERSION=	3.3.2
CATEGORIES=	graphics

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	GPU & Accelerator process monitoring
WWW=		https://github.com/Syllo/nvtop

LICENSE=	GPLv3

USES=		cmake ncurses pkgconfig
USE_GITHUB=	yes
GH_ACCOUNT=	Syllo
GH_PROJECT=	nvtop

BUILD_DEPENDS=	libdrm>0:graphics/libdrm \
		libsysinfo>0:devel/libsysinfo
LIB_DEPENDS=	libudev.so:devel/libudev-devd

.include <bsd.port.mk>
