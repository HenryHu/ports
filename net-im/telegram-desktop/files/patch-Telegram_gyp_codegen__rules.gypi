--- Telegram/gyp/codegen_rules.gypi.orig	2018-02-06 06:53:18 UTC
+++ Telegram/gyp/codegen_rules.gypi
@@ -15,7 +15,7 @@
       '<(SHARED_INTERMEDIATE_DIR)/update_dependent_styles.timestamp',
     ],
     'action': [
-      'python', '<(DEPTH)/update_dependent.py', '--styles',
+      '%%PYTHON_CMD%%', '<(DEPTH)/update_dependent.py', '--styles',
       '-I', '<(res_loc)', '-I', '<(src_loc)',
       '-o', '<(SHARED_INTERMEDIATE_DIR)/update_dependent_styles.timestamp',
       '<@(style_files)',
@@ -26,13 +26,13 @@
     'inputs': [
       '<(DEPTH)/update_dependent.py',
       '<@(qrc_files)',
-      '<!@(python <(DEPTH)/update_dependent.py --qrc_list <@(qrc_files))',
+      '<!@(%%PYTHON_CMD%% <(DEPTH)/update_dependent.py --qrc_list <@(qrc_files))',
     ],
     'outputs': [
       '<(SHARED_INTERMEDIATE_DIR)/update_dependent_qrc.timestamp',
     ],
     'action': [
-      'python', '<(DEPTH)/update_dependent.py', '--qrc',
+      '%%PYTHON_CMD%%', '<(DEPTH)/update_dependent.py', '--qrc',
       '-o', '<(SHARED_INTERMEDIATE_DIR)/update_dependent_qrc.timestamp',
       '<@(qrc_files)',
     ],
@@ -109,7 +109,7 @@
       '<(SHARED_INTERMEDIATE_DIR)/scheme.h',
     ],
     'action': [
-      'python', '<(src_loc)/codegen/scheme/codegen_scheme.py',
+      '%%PYTHON_CMD%%', '<(src_loc)/codegen/scheme/codegen_scheme.py',
       '-o', '<(SHARED_INTERMEDIATE_DIR)', '<(res_loc)/scheme.tl',
     ],
     'message': 'codegen_scheme-ing scheme.tl..',
