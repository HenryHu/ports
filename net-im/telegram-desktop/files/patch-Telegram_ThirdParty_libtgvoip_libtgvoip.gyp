--- Telegram/ThirdParty/libtgvoip/libtgvoip.gyp.orig	2018-02-06 06:51:56 UTC
+++ Telegram/ThirdParty/libtgvoip/libtgvoip.gyp
@@ -13,11 +13,12 @@
         'variables': {
           'tgvoip_src_loc': '.',
           'official_build_target%': '',
-          'linux_path_opus_include%': '<(DEPTH)/../../../Libraries/opus/include',
+          'linux_path_opus_include%': '%%LOCALBASE%%/include/opus',
         },
         'include_dirs': [
           '<(tgvoip_src_loc)/webrtc_dsp',
           '<(linux_path_opus_include)',
+          '%%LOCALBASE%%/include/',
         ],
         'direct_dependent_settings': {
           'include_dirs': [
@@ -378,12 +379,13 @@
             },
           ],
           [
-            '"<(OS)" == "linux"', {
+            '"<(OS)" == "freebsd"', {
               'defines': [
                 'WEBRTC_POSIX',
               ],
               'cflags_cc': [
                 '-msse2',
+                '-std=c++11',
               ],
               'direct_dependent_settings': {
                 'libraries': [
