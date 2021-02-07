--- Telegram/lib_base/base/zlib_help.h.orig	2021-01-28 15:30:24 UTC
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
