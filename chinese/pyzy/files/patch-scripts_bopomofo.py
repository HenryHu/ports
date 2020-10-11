--- scripts/bopomofo.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/bopomofo.py
@@ -446,7 +446,7 @@ bopomofo_pinyin_map = {
     "ㄩㄥ" : "yong",
 }
 
-pinyin_bopomofo_map = dict([(v, k) for k, v in bopomofo_pinyin_map.items()])
+pinyin_bopomofo_map = dict([(v, k) for k, v in list(bopomofo_pinyin_map.items())])
 
 sheng_yun_bopomofo_map = {
     "b" : "ㄅ",
