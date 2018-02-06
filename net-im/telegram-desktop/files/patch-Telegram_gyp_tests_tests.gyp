--- Telegram/gyp/tests/tests.gyp.orig	2018-02-06 06:53:50 UTC
+++ Telegram/gyp/tests/tests.gyp
@@ -13,7 +13,7 @@
     'src_loc': '../../SourceFiles',
     'submodules_loc': '../../ThirdParty',
     'mac_target': '10.10',
-    'list_tests_command': 'python <(DEPTH)/tests/list_tests.py --input <(DEPTH)/tests/tests_list.txt',
+    'list_tests_command': '%%PYTHON_CMD%% <(DEPTH)/tests/list_tests.py --input <(DEPTH)/tests/tests_list.txt',
   },
   'targets': [{
     'target_name': 'tests',
