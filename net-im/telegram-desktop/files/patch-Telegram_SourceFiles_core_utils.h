--- Telegram/SourceFiles/core/utils.h.orig	2018-02-07 00:54:16 UTC
+++ Telegram/SourceFiles/core/utils.h
@@ -464,6 +464,7 @@ enum DBIPlatform {
 	dbipLinux64 = 2,
 	dbipLinux32 = 3,
 	dbipMacOld = 4,
+	dbipFreeBSD = 5,
 };
 
 enum DBIPeerReportSpamStatus {
