--- Telegram/gyp/qt.gypi.orig	2018-01-03 10:46:01 UTC
+++ Telegram/gyp/qt.gypi
@@ -14,25 +14,21 @@
               [ 'build_macold', {
                 'qt_version%': '5.3.2',
               }, {
-                'qt_version%': '5.6.2',
+                'qt_version%': '%%QT_VERSION%%',
               }]
             ],
           },
           'qt_libs': [
-            'qwebp',
-            'Qt5PrintSupport',
-            'Qt5PlatformSupport',
             'Qt5Network',
             'Qt5Widgets',
             'Qt5Gui',
-            'qtharfbuzzng',
           ],
           'qt_version%': '<(qt_version)',
           'conditions': [
             [ 'build_macold', {
               'linux_path_qt%': '/usr/local/macold/Qt-<(qt_version)',
             }, {
-              'linux_path_qt%': '/usr/local/tdesktop/Qt-<(qt_version)',
+              'linux_path_qt%': '%%LOCALBASE%%/lib/qt',
             }]
           ]
         },
@@ -72,44 +68,25 @@
             ],
           }],
           [ 'build_linux', {
-            'qt_lib_prefix': 'lib',
-            'qt_lib_debug_postfix': '.a',
-            'qt_lib_release_postfix': '.a',
+            'qt_lib_prefix': '',
+            'qt_lib_debug_postfix': '',
+            'qt_lib_release_postfix': '',
             'qt_libs': [
-              'qxcb',
-              'Qt5XcbQpa',
-              'qconnmanbearer',
-              'qgenericbearer',
-              'qnmbearer',
               '<@(qt_libs)',
               'Qt5DBus',
               'Qt5Core',
-              'qtpcre',
-              'Xi',
-              'Xext',
-              'Xfixes',
-              'SM',
-              'ICE',
-              'fontconfig',
-              'expat',
-              'freetype',
-              'z',
-              'xcb-shm',
-              'xcb-xfixes',
-              'xcb-render',
-              'xcb-static',
             ],
           }],
         ],
       },
       'qt_version%': '<(qt_version)',
       'qt_loc_unix': '<(qt_loc_unix)',
-      'qt_version_loc': '<!(python -c "print(\'<(qt_version)\'.replace(\'.\', \'_\'))")',
+      'qt_version_loc': '<!(%%PYTHON_CMD%% -c "print(\'<(qt_version)\'.replace(\'.\', \'_\'))")',
       'qt_libs_debug': [
-        '<!@(python -c "for s in \'<@(qt_libs)\'.split(\' \'): print(\'<(qt_lib_prefix)\' + s + \'<(qt_lib_debug_postfix)\')")',
+        '<!@(%%PYTHON_CMD%% -c "for s in \'<@(qt_libs)\'.split(\' \'): print(\'<(qt_lib_prefix)\' + s + \'<(qt_lib_debug_postfix)\')")',
       ],
       'qt_libs_release': [
-        '<!@(python -c "for s in \'<@(qt_libs)\'.split(\' \'): print(\'<(qt_lib_prefix)\' + s + \'<(qt_lib_release_postfix)\')")',
+        '<!@(%%PYTHON_CMD%% -c "for s in \'<@(qt_libs)\'.split(\' \'): print(\'<(qt_lib_prefix)\' + s + \'<(qt_lib_release_postfix)\')")',
       ],
     },
     'qt_libs_debug': [ '<@(qt_libs_debug)' ],
@@ -127,11 +104,6 @@
     # '<!@(python <(DEPTH)/list_sources.py [sources] <(qt_moc_list_sources_arg))'
     # where [sources] contains all your source files
     'qt_moc_list_sources_arg': '--moc-prefix SHARED_INTERMEDIATE_DIR/<(_target_name)/moc/moc_',
-
-    'linux_path_xkbcommon%': '/usr/local',
-    'linux_lib_ssl%': '/usr/local/ssl/lib/libssl.a',
-    'linux_lib_crypto%': '/usr/local/ssl/lib/libcrypto.a',
-    'linux_lib_icu%': 'libicutu.a libicui18n.a libicuuc.a libicudata.a',
   },
 
   'configurations': {
@@ -180,18 +152,18 @@
   },
 
   'include_dirs': [
-    '<(qt_loc)/include',
-    '<(qt_loc)/include/QtCore',
-    '<(qt_loc)/include/QtGui',
-    '<(qt_loc)/include/QtDBus',
-    '<(qt_loc)/include/QtCore/<(qt_version)',
-    '<(qt_loc)/include/QtGui/<(qt_version)',
-    '<(qt_loc)/include/QtCore/<(qt_version)/QtCore',
-    '<(qt_loc)/include/QtGui/<(qt_version)/QtGui',
+    '%%QT_INCDIR%%',
+    '%%QT_INCDIR%%/QtCore',
+    '%%QT_INCDIR%%/QtGui',
+    '%%QT_INCDIR%%/QtDBus',
+    '%%QT_INCDIR%%/QtCore/<(qt_version)',
+    '%%QT_INCDIR%%/QtGui/<(qt_version)',
+    '%%QT_INCDIR%%/QtCore/<(qt_version)/QtCore',
+    '%%QT_INCDIR%%/QtGui/<(qt_version)/QtGui',
   ],
   'library_dirs': [
-    '<(qt_loc)/lib',
-    '<(qt_loc)/plugins',
+    '%%LOCALBASE%%/lib',
+    '%%QT_LIBDIR%%/',
     '<(qt_loc)/plugins/bearer',
     '<(qt_loc)/plugins/platforms',
     '<(qt_loc)/plugins/imageformats',
@@ -212,25 +184,16 @@
       ],
       'libraries': [
         '<(PRODUCT_DIR)/obj.target/liblinux_glibc_wraps.a',
-        '<(linux_path_xkbcommon)/lib/libxkbcommon.a',
         '<@(qt_libs_release)',
-        '<(linux_lib_ssl)',
-        '<(linux_lib_crypto)',
-        '<!@(python -c "for s in \'<(linux_lib_icu)\'.split(\' \'): print(s)")',
-        '-lxcb',
+        '-lcrypto',
         '-lX11',
-        '-lX11-xcb',
-        '-ldbus-1',
-        '-ldl',
-        '-lgthread-2.0',
         '-lglib-2.0',
         '-lpthread',
       ],
       'include_dirs': [
-        '<(qt_loc)/mkspecs/linux-g++',
+        '%%QMAKESPEC%%',
       ],
       'ldflags': [
-        '-static-libstdc++',
         '-pthread',
         '-rdynamic',
       ],
