--- Telegram/SourceFiles/config.h.orig	2018-02-06 05:51:58 UTC
+++ Telegram/SourceFiles/config.h
@@ -242,7 +242,7 @@ inline const char *cApiDeviceModel() {
 	return "PC";
 #elif defined Q_OS_MAC
 	return "Mac";
-#elif defined Q_OS_LINUX
+#elif defined Q_OS_LINUX || defined Q_OS_FREEBSD
 	return "PC";
 #endif
 }
@@ -253,6 +253,8 @@ inline const char *cApiSystemVersion() {
 	return "OS X";
 #elif defined Q_OS_LINUX
 	return "Linux";
+#elif defined Q_OS_FREEBSD
+	return "FreeBSD";
 #endif
 }
 
