--- airscan.h.orig	2020-03-20 13:47:50 UTC
+++ airscan.h
@@ -25,7 +25,7 @@
 
 /* Standard SANE configuration directory
  */
-#define CONFIG_SANE_CONFIG_DIR          "/etc/sane.d/"
+#define CONFIG_SANE_CONFIG_DIR          LOCALBASE "/etc/sane.d/"
 
 /* Sane-airscan configuration file and subdirectory names
  */
