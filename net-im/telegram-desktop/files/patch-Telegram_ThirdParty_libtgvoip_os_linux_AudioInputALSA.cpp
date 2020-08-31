--- Telegram/ThirdParty/libtgvoip/os/linux/AudioInputALSA.cpp.orig	2020-08-18 07:13:47 UTC
+++ Telegram/ThirdParty/libtgvoip/os/linux/AudioInputALSA.cpp
@@ -12,6 +12,10 @@
 #include "../../logging.h"
 #include "../../VoIPController.h"
 
+#ifndef typeof
+#define typeof __typeof__
+#endif
+
 using namespace tgvoip::audio;
 
 #define BUFFER_SIZE 960
