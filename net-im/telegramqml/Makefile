# Created by: Henry Hu <henry.hu.sh@gmail.com>
# $FreeBSD$

PORTNAME=	telegramqml
PORTVERSION=	0.9.1
CATEGORIES=	net-im
MASTER_SITES=	https://github.com/${GH_ACCOUNT}/${GH_PROJECT}/archive/ \
		http://github.com/${GH_ACCOUNT}/${GH_PROJECT}/archive/
DISTNAME=	v${GH_RELEASE}

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	Fork of libqtelegram by Aseman Team

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libqtelegram-ae.so:${PORTSDIR}/net-im/libqtelegram-ae

GH_ACCOUNT=	Aseman-Land
GH_PROJECT=	TelegramQML
GH_RELEASE=	${PORTVERSION}-stable
WRKSRC=		${WRKDIR}/${GH_PROJECT}-${GH_RELEASE}

USES=		qmake:outsource
USE_QT5=	qmake_build buildtools_build core qml quick sql xml multimedia
USE_LDCONFIG=	yes
QMAKE_ARGS=	BUILD_MODE+=lib

.include <bsd.port.mk>
