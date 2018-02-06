# $FreeBSD$

PORTNAME=	range-v3
PORTVERSION=	0.3.0
CATEGORIES=	devel

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	Experimental range library for C++11/14/17

LICENSE=	BSL
LICENSE_FILE=	${WRKSRC}/LICENSE.txt

USES=		cmake
USE_GITHUB=	yes
GH_ACCOUNT=	ericniebler

OPTIONS_DEFINE=	TEST MODULES
OPTIONS_DEFAULT=

MODULES_DESC=	Enables Clang Modules
TEST_DESC=	Build the testing tree

TEST_CMAKE_OFF=	-DBUILD_TESTING:BOOL=OFF
MODULES_CMAKE_ON=	-DRANGES_MODULES:BOOL=ON

.include <bsd.port.pre.mk>

.if ${OPSYS} == FreeBSD && ${OSVERSION} < 1100000
CC=		clang40
CXX=		clang++40
BUILD_DEPENDS+=	clang++40:devel/llvm40
RUN_DEPENDS+=	clang++40:devel/llvm40
.endif

.include <bsd.port.post.mk>
