# $FreeBSD: head/devel/range-v3/Makefile 528005 2020-03-08 08:32:15Z tcberner $

PORTNAME=	range-v3
DISTVERSION=	0.10.0
CATEGORIES=	devel

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	Experimental range library for C++11/14/17

LICENSE=	BSL
LICENSE_FILE=	${WRKSRC}/LICENSE.txt

USES=		cmake
USE_GITHUB=	yes
GH_ACCOUNT=	ericniebler
NO_ARCH=	yes

OPTIONS_DEFINE=	TESTS EXAMPLES
OPTIONS_DEFAULT=

TESTS_DESC=	Build tests
EXAMPLES_DESC=	Build examples

TESTS_CMAKE_BOOL=	RANGE_V3_TESTS
EXAMPLES_CMAKE_BOOL=	RANGE_V3_EXAMPLES

post-install:
	@${RM} ${STAGEDIR}${PREFIX}/include/module.modulemap

test:
	@${MAKE_CMD} -C ${TEST_WRKSRC} test

.include <bsd.port.mk>
