# Created by: Henry Hu <henry.hu.sh@gmail.com>
# $FreeBSD$

PORTNAME=	desktop-app-rlottie
PORTVERSION=	0.0.20201025
CATEGORIES=	devel

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	A platform independent standalone library that plays Lottie Animation.

LICENSE=	LGPL21 FTL MIT RPD PD
LICENSE_COMB=	multi
LICENSE_FILE_LGPL21=	${WRKSRC}/licenses/COPYING.LGPL
LICENSE_FILE_FTL=	${WRKSRC}/licenses/COPYING.FTL
LICENSE_NAME_FTL=	The FreeType Project LICENSE
LICENSE_PERMS_FTL=	dist-mirror dist-sell pkg-mirror pkg-sell auto-accept
LICENSE_FILE_MIT=	${WRKSRC}/licenses/COPYING.PIX
LICENSE_FILE_RPD=	${WRKSRC}/licenses/COPYING.RPD
LICENSE_NAME_RPD=	RapidJSON
LICENSE_PERMS_RPD=	dist-mirror dist-sell pkg-mirror pkg-sell auto-accept

USES=		cmake
USE_LDCONFIG=	yes
USE_GITHUB=	yes
GH_ACCOUNT=	desktop-app
GH_PROJECT=	rlottie
GH_TAGNAME=	839dcab

CMAKE_ARGS=	-DLIB_INSTALL_DIR=${LOCALBASE}/lib

.include <bsd.port.mk>
