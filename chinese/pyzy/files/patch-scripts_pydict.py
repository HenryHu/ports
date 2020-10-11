--- scripts/pydict.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/pydict.py
@@ -119,10 +119,10 @@ PINYIN_DICT = {
     #~ "eng" : 411, "chua" : 412, "fe" : 413, "fiao" : 414, "liong" : 415
 }
 
-PINYIN_LIST = PINYIN_DICT.keys ()
+PINYIN_LIST = list(PINYIN_DICT.keys ())
 
 ID_PINYIN_DICT = {}
-for pinyin, id in PINYIN_DICT.items ():
+for pinyin, id in list(PINYIN_DICT.items ()):
     ID_PINYIN_DICT[id] = pinyin
 
 SHENGMU_DICT = {
@@ -131,7 +131,7 @@ SHENGMU_DICT = {
     "j" : 12, "q" : 13, "x" : 14, "zh" : 15, "ch" : 16, "sh" : 17,
     "r" : 18, "z" : 19, "c" : 20, "s" : 21, "y" : 22, "w" : 23
 }
-SHENGMU_LIST = SHENGMU_DICT.keys ()
+SHENGMU_LIST = list(SHENGMU_DICT.keys ())
 #~ PINYIN_PARTIAL_LIST = []
 #~ for p in PINYIN_LIST:
     #~ for i in range (2, len (p)):
@@ -151,7 +151,7 @@ PINYIN_PARTIAL_LIST = [
 ID_SHENGMU_DICT = {}
 
 
-for shengmu, id in SHENGMU_DICT.items ():
+for shengmu, id in list(SHENGMU_DICT.items ()):
     ID_SHENGMU_DICT[id] = shengmu
 
 MOHU_SHENGMU = {
