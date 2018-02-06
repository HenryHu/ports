--- Telegram/gyp/qt_rcc.gypi.orig	2018-01-03 10:46:01 UTC
+++ Telegram/gyp/qt_rcc.gypi
@@ -15,7 +15,7 @@
       '<(SHARED_INTERMEDIATE_DIR)/<(_target_name)/qrc/qrc_<(RULE_INPUT_ROOT).cpp',
     ],
     'action': [
-      '<(qt_loc)/bin/rcc<(exe_ext)',
+      '%%QT_BINDIR%%/rcc',
       '-name', '<(RULE_INPUT_ROOT)',
       '-no-compress',
       '<(RULE_INPUT_PATH)',
