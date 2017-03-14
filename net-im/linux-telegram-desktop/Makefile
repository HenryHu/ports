# Created by: Henry Hu <henry.hu.sh@gmail.com>
# $FreeBSD$

PORTNAME=	linux-telegram-desktop
PORTVERSION=	1.0.14
CATEGORIES=	net-im
MASTER_SITES=	https://updates.tdesktop.com/tlinux32/
DISTNAME=	tsetup32.${PORTVERSION}

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	Telegram Desktop client

LICENSE=	GPLv3

NO_BUILD=	yes

USES=		linux:c7 tar:xz
USE_LINUX=	alsalib alsa-plugins-oss dbuslibs dri expat gtk2 xorglibs
RESTRICTED=	Redistribution prohibited.

WRKSRC=		${WRKDIR}/Telegram
TDESKTOPDIR=	lib/tdesktop
PLIST_SUB+=	TDESKTOPDIR=${TDESKTOPDIR}
SUB_FILES=	tdesktop.sh
SUB_LIST+=	TDESKTOPDIR=${TDESKTOPDIR}

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/${TDESKTOPDIR}
# The binary main program
	@${INSTALL_PROGRAM} ${WRKSRC}/Telegram ${STAGEDIR}${PREFIX}/${TDESKTOPDIR}/

# The wrapper for main program
	@${INSTALL_SCRIPT} ${WRKDIR}/tdesktop.sh ${STAGEDIR}${PREFIX}/bin/tdesktop

.include <bsd.port.mk>
