# Created by: Henry Hu <henry.hu.sh@gmail.com>
# $FreeBSD$

PORTNAME=	libqtelegram-ae
PORTVERSION=	6.0
CATEGORIES=	net-im
MASTER_SITES=	https://github.com/${GH_ACCOUNT}/${GH_PROJECT}/archive/ \
		http://github.com/${GH_ACCOUNT}/${GH_PROJECT}/archive/
DISTNAME=	v${PORTVERSION}

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	Fork of libqtelegram by Aseman Team

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

GH_ACCOUNT=	Aseman-Land
GH_PROJECT=	libqtelegram-aseman-edition
WRKSRC=		${WRKDIR}/${GH_PROJECT}-${PORTVERSION}

USES=		qmake:outsource
USE_QT5=	qmake_build buildtools_build gui network multimedia
USE_LDCONFIG=	yes

.include <bsd.port.mk>
