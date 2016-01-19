# $FreeBSD: head/sysutils/synergy/Makefile 406147 2016-01-15 09:27:50Z kevlo $

PORTNAME=	synergy
PORTVERSION=	1.7.5
PORTREVISION=	1
CATEGORIES=	sysutils

MAINTAINER=	kevlo@FreeBSD.org
COMMENT=	Mouse and keyboard sharing utility

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		cmake cpe
CPE_VENDOR=	synergy-foss
USE_XORG=	ice xtst x11 sm
USE_GITHUB=	yes

DISTVERSIONPREFIX=	v
DISTVERSIONSUFFIX=	-stable

LIB_DEPENDS=	libcurl.so:${PORTSDIR}/ftp/curl

MAKE_JOBS_UNSAFE=yes

CFLAGS+=	-I${LOCALBASE}/include -L${LOCALBASE}/lib

PLIST_FILES=    bin/synergyc bin/synergyd bin/synergys \
		lib/synergy/libns.so man/man1/synergyc.1.gz man/man1/synergys.1.gz
PORTEXAMPLES=	synergy.conf.example synergy.conf.example-basic \
		synergy.conf.example-advanced

OPTIONS_DEFINE=	EXAMPLES

BROKEN_sparc64=	cannot build: C++ code errors

do-install:
.for f in synergyc synergyd synergys
	${INSTALL_PROGRAM} ${WRKSRC}/bin/${f} ${STAGEDIR}${PREFIX}/bin
.endfor
	${MKDIR} ${STAGEDIR}${PREFIX}/lib/synergy
	${INSTALL_LIB} ${WRKSRC}/lib/libns.so ${STAGEDIR}${PREFIX}/lib/synergy
	${INSTALL_MAN} ${WRKSRC}/doc/synergyc.man \
		${STAGEDIR}${MANPREFIX}/man/man1/synergyc.1
	${INSTALL_MAN} ${WRKSRC}/doc/synergys.man \
		${STAGEDIR}${MANPREFIX}/man/man1/synergys.1
	${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
.for f in ${PORTEXAMPLES}
	${INSTALL_DATA} ${WRKSRC}/doc/${f} ${STAGEDIR}${EXAMPLESDIR}
.endfor

.include <bsd.port.mk>
