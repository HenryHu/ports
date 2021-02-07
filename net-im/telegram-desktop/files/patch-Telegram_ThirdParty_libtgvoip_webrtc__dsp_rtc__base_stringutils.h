--- Telegram/ThirdParty/libtgvoip/webrtc_dsp/rtc_base/stringutils.h.orig	2021-01-01 14:29:15 UTC
+++ Telegram/ThirdParty/libtgvoip/webrtc_dsp/rtc_base/stringutils.h
@@ -25,7 +25,7 @@
 #endif  // WEBRTC_WIN
 
 #if defined(WEBRTC_POSIX)
-#ifdef BSD
+#ifdef __FreeBSD__
 #include <stdlib.h>
 #else  // BSD
 #include <alloca.h>
