# Created by: Anders F Bjorklund <afb@users.sourceforge.net>
# $FreeBSD: head/ports-mgmt/packagekit/Makefile 496006 2019-03-17 00:04:52Z tcberner $
#   $MCom: ports/ports-mgmt/packagekit/Makefile,v 1.26 2010/10/10 15:49:51 marcus Exp $

PORTNAME=	PackageKit
PORTVERSION=	1.1.12
CATEGORIES=	ports-mgmt sysutils
MASTER_SITES=	http://www.freedesktop.org/software/PackageKit/releases/

MAINTAINER=	gnome@FreeBSD.org
COMMENT?=	DBUS packaging abstraction layer

LIB_DEPENDS=	libdbus-glib-1.so:devel/dbus-glib \
		libpolkit-gobject-1.so:sysutils/polkit \
		libck-connector.so:sysutils/consolekit2
RUN_DEPENDS=	lsof:sysutils/lsof \
		bash:shells/bash

USES=		cpe gettext gmake iconv libtool pathfix pkgconfig \
		python:build shared-mime-info shebangfix sqlite:3 tar:xz
CPE_VENDOR=	packagekit_project
SHEBANG_FILES=	backends/test/helpers/search-name.sh \
		contrib/cron/packagekit-background.cron
USE_GNOME=	glib20 intltool introspection
USE_LDCONFIG=	yes
GNU_CONFIGURE=	yes
LIBS+=		-lexecinfo
CONFIGURE_ARGS+=--with-security-framework=polkit \
		--localstatedir=/var \
		--disable-static \
		--disable-gtk-doc \
		--disable-managed \
		--disable-browser-plugin \
		--disable-gstreamer-plugin \
		--disable-networkmanager \
		--disable-connman \
		--disable-systemd
INSTALL_TARGET=	install-strip

MAKE_JOBS_UNSAFE=yes

.if !defined(SLAVEPORT)
OPTIONS_DEFINE=	PORTS MANPAGES DOCS BASH
OPTIONS_DEFAULT=PORTS
PORTS_DESC=Use portupgrade for management, dummy if disabled
BASH_DESC=Install bash completion for PackageKit

.include <bsd.port.options.mk>

. if ${PORT_OPTIONS:MMANPAGES}
BUILD_DEPENDS+=	docbook-sgml>0:textproc/docbook-sgml \
		xsltproc:textproc/libxslt \
		${LOCALBASE}/share/xsl/docbook/manpages/docbook.xsl:textproc/docbook-xsl
PLIST_SUB+=	MAN=''
. else
CONFIGURE_ARGS+=--disable-man-pages
PLIST_SUB+=	MAN='@comment '
. endif

. if ${PORT_OPTIONS:MDOCS}
CONFIGURE_ARGS+=--enable-gtk-doc-html
PLIST_SUB+=	DOCS=''
. else
CONFIGURE_ARGS+=--disable-gtk-doc-html
PLIST_SUB+=	DOCS='@comment '
. endif

. if ${PORT_OPTIONS:MPORTS}
RUN_DEPENDS+=	${LOCALBASE}/sbin/portupgrade:ports-mgmt/portupgrade
USE_RUBY=	yes
CONFIGURE_ARGS+=--enable-ports --with-default-backend=ports
PLIST_SUB+=	PORTS=""
. else
CONFIGURE_ARGS+=--disable-ports --with-default-backend=dummy
PLIST_SUB+=	PORTS="@comment "
. endif

CONFIGURE_ARGS+=--disable-gtk-module
PLIST_SUB+=	GTK="@comment "

CONFIGURE_ARGS+=--disable-qt

. if ${PORT_OPTIONS:MBASH}
BUILD_DEPENDS=	bash-completion>0:shells/bash-completion
CONFIGURE_ARGS+=--enable-bash-completion
PLIST_SUB+=	BASH=''
. else
CONFIGURE_ARGS+=--disable-bash-completion
PLIST_SUB+=	BASH='@comment '
. endif
.endif

post-patch:
	@${REINPLACE_CMD} -E -e 's/.*WARNINGFLAGS_CPP.*-Werror/#$$&/' \
		-e 's|-DG_DISABLE_DEPRECATED||g' \
		-e 's|-Wmissing-include-dirs||g' ${WRKSRC}/configure
	@${REINPLACE_CMD} -e 's|girepositry|girepository|g' \
		${WRKSRC}/lib/packagekit-glib2/Makefile.in
	@${REINPLACE_CMD} -e 's|/usr/bin/pkttyagent|${LOCALBASE}/bin/pkttyagent|' \
		-e 's/POLLHUP/POLLHUP | POLLIN/' \
		${WRKSRC}/lib/packagekit-glib2/pk-spawn-polkit-agent.c
	@${FIND} ${WRKSRC} -name Makefile.in | ${XARGS} ${REINPLACE_CMD} -e \
		'/xsltproc/s|.xsl [$$]? &> /dev|.xsl $$? > /dev|g'

post-install:
.if !defined(SLAVEPORT)
	@${INSTALL_DATA} ${WRKSRC}/data/transactions.db \
		${STAGEDIR}${PREFIX}/share/PackageKit/transactions.db
	@${MV} ${STAGEDIR}${PREFIX}/etc/PackageKit/CommandNotFound.conf \
		${STAGEDIR}${PREFIX}/etc/PackageKit/CommandNotFound.conf.default
	@${MV} ${STAGEDIR}${PREFIX}/etc/PackageKit/PackageKit.conf \
		${STAGEDIR}${PREFIX}/etc/PackageKit/PackageKit.conf.default
.endif

.include <bsd.port.mk>
