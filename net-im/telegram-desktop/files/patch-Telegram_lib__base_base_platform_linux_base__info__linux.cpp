--- Telegram/lib_base/base/platform/linux/base_info_linux.cpp.orig	2021-01-28 15:30:24 UTC
+++ Telegram/lib_base/base/platform/linux/base_info_linux.cpp
@@ -14,11 +14,6 @@
 #include <QtCore/QDate>
 #include <QtGui/QGuiApplication>
 
-// this file is used on both Linux & BSD
-#ifdef Q_OS_LINUX
-#include <gnu/libc-version.h>
-#endif // Q_OS_LINUX
-
 namespace Platform {
 namespace {
 
@@ -100,6 +95,15 @@ QString DeviceModelPretty() {
 }
 
 QString SystemVersionPretty() {
+<<<<<<< HEAD
+	const auto result = getenv("XDG_CURRENT_DESKTOP");
+	const auto value = result ? QString::fromLatin1(result) : QString();
+	const auto list = value.split(':', QString::SkipEmptyParts);
+
+	return "FreeBSD "
+		+ (list.isEmpty() ? QString() : list[0] + ' ')
+		+ (IsWayland() ? "Wayland " : "X11 ");
+=======
 	static const auto result = [&] {
 		QStringList resultList{};
 
@@ -138,6 +142,7 @@ QString SystemVersionPretty() {
 	}();
 
 	return result;
+>>>>>>> 2bf29ab1a5458003c8ed250886e08c61cce5ff72
 }
 
 QString SystemCountry() {
@@ -158,10 +163,13 @@ QDate WhenSystemBecomesOutdated() {
 
 	if (IsLinux32Bit()) {
 		return QDate(2020, 9, 1);
+<<<<<<< HEAD
+=======
 	} else if (libcName == qstr("glibc") && !libcVersion.isEmpty()) {
 		if (QVersionNumber::fromString(libcVersion) < QVersionNumber(2, 23)) {
 			return QDate(2020, 9, 1); // Older than Ubuntu 16.04.
 		}
+>>>>>>> 2bf29ab1a5458003c8ed250886e08c61cce5ff72
 	}
 
 	return QDate();
@@ -185,6 +193,8 @@ QString AutoUpdateKey() {
 	}
 }
 
+<<<<<<< HEAD
+=======
 QString GetLibcName() {
 #ifdef Q_OS_LINUX
 	return "glibc";
@@ -205,6 +215,7 @@ QString GetLibcVersion() {
 	return QString();
 }
 
+>>>>>>> 2bf29ab1a5458003c8ed250886e08c61cce5ff72
 bool IsWayland() {
 	return QGuiApplication::instance()
 		? QGuiApplication::platformName().startsWith(
