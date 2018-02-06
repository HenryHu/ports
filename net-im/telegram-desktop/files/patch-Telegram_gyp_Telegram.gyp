--- Telegram/gyp/Telegram.gyp.orig	2018-01-03 10:46:01 UTC
+++ Telegram/gyp/Telegram.gyp
@@ -49,7 +49,7 @@
         'pt-BR',
       ],
       'build_defines%': '',
-      'list_sources_command': 'python <(DEPTH)/list_sources.py --input <(DEPTH)/telegram_sources.txt --replace src_loc=<(src_loc)',
+      'list_sources_command': '%%PYTHON_CMD%% <(DEPTH)/list_sources.py --input <(DEPTH)/telegram_sources.txt --replace src_loc=<(src_loc)',
     },
     'includes': [
       'common_executable.gypi',
@@ -69,30 +69,20 @@
       'codegen.gyp:codegen_numbers',
       'codegen.gyp:codegen_style',
       'tests/tests.gyp:tests',
-      'utils.gyp:Updater',
       '../ThirdParty/libtgvoip/libtgvoip.gyp:libtgvoip',
       'crl.gyp:crl',
     ],
 
     'defines': [
-      'AL_LIBTYPE_STATIC',
       'AL_ALEXT_PROTOTYPES',
       'TGVOIP_USE_CXX11_LIB',
-      '<!@(python -c "for s in \'<(build_defines)\'.split(\',\'): print(s)")',
+      '<!@(%%PYTHON_CMD%% -c "for s in \'<(build_defines)\'.split(\',\'): print(s)")',
     ],
 
     'include_dirs': [
       '<(src_loc)',
       '<(SHARED_INTERMEDIATE_DIR)',
-      '<(libs_loc)/breakpad/src',
-      '<(libs_loc)/lzma/C',
-      '<(libs_loc)/zlib',
-      '<(libs_loc)/ffmpeg',
-      '<(libs_loc)/openal-soft/include',
-      '<(libs_loc)/opus/include',
-      '<(libs_loc)/range-v3/include',
-      '<(minizip_loc)',
-      '<(sp_media_key_tap_loc)',
+      '%%LOCALBASE%%/minizip',
       '<(emoji_suggestions_loc)',
       '<(submodules_loc)/GSL/include',
       '<(submodules_loc)/variant/include',
@@ -105,7 +95,7 @@
       'telegram_sources.txt',
     ],
     'sources!': [
-      '<!@(<(list_sources_command) <(qt_moc_list_sources_arg) --exclude_for <(build_os))',
+      '<!@(<(list_sources_command) <(qt_moc_list_sources_arg) --exclude_for linux)',
     ],
     'conditions': [
       [ '"<(official_build_target)" != ""', {
