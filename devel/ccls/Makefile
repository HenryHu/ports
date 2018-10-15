# $FreeBSD$

PORTNAME=	ccls
PORTVERSION=	0.20181010
CATEGORIES=	devel

MAINTAINER=	henry.hu.sh@gmail.com
COMMENT=	C/C++/Objective-C language server

LICENSE=	MIT

BROKEN_powerpc64=	fails to build: Checking for 'clang++' (C++ compiler): not found

BUILD_DEPENDS=	llvm-config60:devel/llvm60

USES=		compiler:c++17-lang cmake

USE_GITHUB=	yes
GH_ACCOUNT=	MaskRay
GH_TUPLE=	Tencent:rapidjson:6a905f9:rapidjson/third_party/rapidjson

PLIST_FILES=	bin/ccls

CMAKE_ARGS+=	-DSYSTEM_CLANG=ON -DCLANG_ROOT=${PREFIX}/llvm60

.include <bsd.port.mk>
