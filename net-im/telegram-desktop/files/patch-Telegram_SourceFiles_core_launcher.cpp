--- Telegram/SourceFiles/core/launcher.cpp.orig	2019-06-01 09:44:13 UTC
+++ Telegram/SourceFiles/core/launcher.cpp
@@ -15,6 +15,8 @@ https://github.com/telegramdesktop/tdesktop/blob/maste
 #include "core/sandbox.h"
 #include "base/concurrent_timer.h"
 
+#include "FREEBSD_QT_PLUGINDIR.h"
+
 namespace Core {
 namespace {
 
@@ -245,12 +247,13 @@ void Launcher::init() {
 #define TDESKTOP_LAUNCHER_FILENAME_TO_STRING_HELPER(V) #V
 #define TDESKTOP_LAUNCHER_FILENAME_TO_STRING(V) TDESKTOP_LAUNCHER_FILENAME_TO_STRING_HELPER(V)
 	QApplication::setDesktopFileName(qsl(TDESKTOP_LAUNCHER_FILENAME_TO_STRING(TDESKTOP_LAUNCHER_FILENAME)));
-#elif defined(Q_OS_LINUX) && QT_VERSION >= QT_VERSION_CHECK(5, 7, 0)
+#elif (defined(Q_OS_LINUX) || defined(Q_OS_FREEBSD)) && QT_VERSION >= QT_VERSION_CHECK(5, 7, 0)
 	QApplication::setDesktopFileName(qsl("telegramdesktop.desktop"));
 #endif
-#ifndef OS_MAC_OLD
+#if !defined(Q_OS_MAC) && QT_VERSION >= QT_VERSION_CHECK(5, 6, 0)
+	// Retina display support is working fine, others are not.
 	QApplication::setAttribute(Qt::AA_DisableHighDpiScaling, true);
-#endif // OS_MAC_OLD
+#endif // not defined Q_OS_MAC and QT_VERSION >= 5.6.0
 
 	initHook();
 }
@@ -268,6 +271,11 @@ int Launcher::exec() {
 	Logs::start(this); // must be started before Platform is started
 	Platform::start(); // must be started before Sandbox is created
 
+	// I don't know why path is not in QT_PLUGIN_PATH by default
+	QCoreApplication::addLibraryPath(FREEBSD_QT_PLUGINDIR);
+	// Telegram doesn't start when extraordinary theme is set, see launchpad.net/bugs/1680943
+	unsetenv("QT_QPA_PLATFORMTHEME");
+
 	auto result = executeApplication();
 
 	DEBUG_LOG(("Telegram finished, result: %1").arg(result));
@@ -369,6 +377,9 @@ void Launcher::prepareSettings() {
 	break;
 	case dbipLinux32:
 		gPlatformString = qsl("Linux32bit");
+	break;
+	case dbipFreeBSD:
+		gPlatformString = qsl("FreeBSD");
 	break;
 	}
 
