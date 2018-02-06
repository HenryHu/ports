--- Telegram/gyp/linux_glibc_wraps.gyp.orig	2018-01-03 10:46:01 UTC
+++ Telegram/gyp/linux_glibc_wraps.gyp
@@ -14,7 +14,7 @@
     'sources': [
       '../SourceFiles/platform/linux/linux_glibc_wraps.c',
     ],
-    'conditions': [[ '"<!(uname -p)" == "x86_64"', {
+    'conditions': [[ '"<!(uname -m)" == "x86_64"', {
       'sources': [
         '../SourceFiles/platform/linux/linux_glibc_wraps_64.c',
       ],
