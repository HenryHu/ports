--- Telegram/gyp/telegram_linux.gypi.orig	2018-01-03 10:46:01 UTC
+++ Telegram/gyp/telegram_linux.gypi
@@ -20,10 +20,11 @@
       'linux_path_va%': '/usr/local',
       'linux_path_vdpau%': '/usr/local',
       'linux_path_breakpad%': '/usr/local',
-      'linux_path_opus_include%': '<(libs_loc)/opus/include',
+      'linux_path_opus_include%': '%%LOCALBASE%%/include/opus',
       'linux_path_range%': '/usr/local',
     },
     'include_dirs': [
+      '/usr/include/openssl-1.0',
       '/usr/local/include',
       '<(linux_path_ffmpeg)/include',
       '<(linux_path_openal)/include',
@@ -32,6 +33,7 @@
       '<(linux_path_range)/include',
     ],
     'library_dirs': [
+      '/usr/lib/openssl-1.0',
       '/usr/local/lib',
       '<(linux_path_ffmpeg)/lib',
       '<(linux_path_openal)/lib',
@@ -40,25 +42,15 @@
       '<(linux_path_breakpad)/lib',
     ],
     'libraries': [
-      'breakpad_client',
-      'composeplatforminputcontextplugin',
-      'ibusplatforminputcontextplugin',
-      'fcitxplatforminputcontextplugin',
-      'himeplatforminputcontextplugin',
-      'liblzma.a',
-      'libopenal.a',
-      'libavformat.a',
-      'libavcodec.a',
-      'libswresample.a',
-      'libswscale.a',
-      'libavutil.a',
-      'libopus.a',
-      'libva-x11.a',
-      'libva-drm.a',
-      'libva.a',
-      'libvdpau.a',
-      'libdrm.a',
-      'libz.a',
+      'openal',
+      'avformat',
+      'avcodec',
+      'swresample',
+      'swscale',
+      'avutil',
+      'minizip',
+      'opus',
+      'z',
 #      '<!(pkg-config 2> /dev/null --libs <@(pkgconfig_libs))',
     ],
     'cflags_cc': [
@@ -86,7 +78,7 @@
       },
     },
     'conditions': [
-      [ '"<!(uname -p)" == "x86_64"', {
+      [ '"<!(uname -m)" == "x86_64"', {
         # 32 bit version can't be linked with debug info or LTO,
         # virtual memory exhausted :(
         'cflags_c': [ '-g' ],
@@ -94,9 +86,9 @@
         'ldflags': [ '-g' ],
         'configurations': {
           'Release': {
-            'cflags_c': [ '-flto' ],
-            'cflags_cc': [ '-flto' ],
-            'ldflags': [ '-flto' ],
+            'cflags_c': [ '%%CFLAGS%%' ],
+            'cflags_cc': [ '%%CXXFLAGS%%' ],
+            'ldflags': [ '%%LDFLAGS%%' ],
           },
         },
       }, {
@@ -105,10 +97,7 @@
         ],
       }], ['not_need_gtk!="True"', {
         'cflags_cc': [
-          '<!(pkg-config 2> /dev/null --cflags appindicator-0.1)',
-          '<!(pkg-config 2> /dev/null --cflags gtk+-2.0)',
-          '<!(pkg-config 2> /dev/null --cflags glib-2.0)',
-          '<!(pkg-config 2> /dev/null --cflags dee-1.0)',
+          '<!(pkg-config 2> /dev/null --cflags gtk+-3.0)',
         ],
       }]
     ],
