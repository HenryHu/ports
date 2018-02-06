--- Telegram/SourceFiles/data/data_document.cpp.orig	2018-02-06 06:23:36 UTC
+++ Telegram/SourceFiles/data/data_document.cpp
@@ -65,7 +65,7 @@ QString saveFileName(const QString &titl
 	name = name.replace(QRegularExpression(qsl("[\\\\\\/\\:\\*\\?\\\"\\<\\>\\|]")), qsl("_"));
 #elif defined Q_OS_MAC
 	name = name.replace(QRegularExpression(qsl("[\\:]")), qsl("_"));
-#elif defined Q_OS_LINUX
+#elif defined Q_OS_LINUX || defined Q_OS_FREEBSD
 	name = name.replace(QRegularExpression(qsl("[\\/]")), qsl("_"));
 #endif
 	if (Global::AskDownloadPath() || savingAs) {
