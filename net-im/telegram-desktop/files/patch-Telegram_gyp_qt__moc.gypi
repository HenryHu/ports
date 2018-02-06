--- Telegram/gyp/qt_moc.gypi.orig	2018-01-03 10:46:01 UTC
+++ Telegram/gyp/qt_moc.gypi
@@ -12,12 +12,12 @@
       '<(SHARED_INTERMEDIATE_DIR)/<(_target_name)/moc/moc_<(RULE_INPUT_ROOT).cpp',
     ],
     'action': [
-      '<(qt_loc)/bin/moc<(exe_ext)',
+      '%%QT_BINDIR%%/moc',
 
       # Silence "Note: No relevant classes found. No output generated."
       '--no-notes',
 
-      '<!@(python -c "for s in \'<@(_defines)\'.split(\' \'): print(\'-D\' + s)")',
+      '<!@(%%PYTHON_CMD%% -c "for s in \'<@(_defines)\'.split(\' \'): print(\'-D\' + s)")',
       # '<!@(python -c "for s in \'<@(_include_dirs)\'.split(\' \'): print(\'-I\' + s)")',
       '<(RULE_INPUT_PATH)',
       '-o', '<(SHARED_INTERMEDIATE_DIR)/<(_target_name)/moc/moc_<(RULE_INPUT_ROOT).cpp',
