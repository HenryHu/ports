--- Telegram/lib_base/base/zlib_help.h.orig	2020-08-10 11:25:13 UTC
+++ Telegram/lib_base/base/zlib_help.h
@@ -6,8 +6,8 @@
 //
 #pragma once
 
-#include <zip.h>
-#include <unzip.h>
+#include "minizip/zip.h"
+#include "minizip/unzip.h"
 #include "logs.h"
 
 #ifdef small
