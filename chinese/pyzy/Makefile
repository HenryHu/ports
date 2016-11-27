# Created by: Henry Hu <henry.hu.sh@gmail.com>
# $FreeBSD: head/chinese/pyzy/Makefile 422140 2016-09-14 15:59:34Z mat $

PORTNAME=	pyzy
PORTVERSION=	0.1.0
PORTREVISION=	3
CATEGORIES=	chinese
MASTER_SITES=	GH
DISTFILES=	${DISTNAME}${EXTRACT_SUFX}
EXTRACT_ONLY=	${DISTNAME}${EXTRACT_SUFX}

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	The Chinese PinYin and Bopomofo conversion library

LICENSE=	LGPL21

LIB_DEPENDS=	libsqlite3.so:databases/sqlite3

USE_GITHUB=	yes
GH_TAGNAME=	6d9c3cd

USES=		compiler:c++11-lib gmake libtool pkgconfig python:build shebangfix autoreconf gettext-runtime
SHEBANG_FILES=	data/db/android/create_db.py
USE_GNOME=	glib20
USE_LDCONFIG=	yes

GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--disable-dependency-tracking --disable-boost

OPTIONS_DEFINE=	ANDROID_DB OPENCC
OPTIONS_DEFAULT=	ANDROID_DB
OPTIONS_SUB=	yes
ANDROID_DB_DESC=	Build Android DB
OPENCC_DESC=		Use opencc for simplified and traditional Chinese conversion

OPENCC_CONFIGURE_ENABLE=	opencc
OPENCC_LIB_DEPENDS=		libopencc.so:chinese/opencc

post-patch:
	@${REINPLACE_CMD} -e 's|$$(libdir)/pkgconfig|${PREFIX}/libdata/pkgconfig|' ${WRKSRC}/Makefile.am

post-install:
	@${STRIP_CMD} ${STAGEDIR}${PREFIX}/lib/lib${PORTNAME}-1.0.so

.include <bsd.port.mk>
