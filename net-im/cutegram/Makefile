# Created by: Henry Hu <henry.hu.sh@gmail.com>
# $FreeBSD$

PORTNAME=	cutegram
PORTVERSION=	2.7.0
CATEGORIES=	net-im
MASTER_SITES=	https://github.com/${GH_ACCOUNT}/${GH_PROJECT}/archive/ \
		http://github.com/${GH_ACCOUNT}/${GH_PROJECT}/archive/
DISTNAME=	v${GH_RELEASE}

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	Free and opensource telegram client

LICENSE=	GPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libqtelegram-ae.so:${PORTSDIR}/net-im/libqtelegram-ae \
			libtelegramqml.so:${PORTSDIR}/net-im/telegramqml

GH_ACCOUNT=	Aseman-Land
GH_PROJECT=	Cutegram
GH_RELEASE=	${PORTVERSION}-stable
WRKSRC=		${WRKDIR}/${GH_PROJECT}-${GH_RELEASE}

USES=		qmake:outsource desktop-file-utils
USE_QT5=	qmake_build buildtools_build core qml quick sql xml multimedia widgets dbus webkit quickcontrols graphicaleffects sql-sqlite3

.include <bsd.port.mk>
