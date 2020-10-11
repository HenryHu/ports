--- scripts/pyutil.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/pyutil.py
@@ -38,7 +38,7 @@ class PinYinWord:
             self._sheng_mu_id = SHENGMU_DICT [self._pinyin]
 
     def is_valid_pinyin (self):
-        return PINYIN_DICT.has_key (self._pinyin)
+        return self._pinyin in PINYIN_DICT
 
     def get_sheng_mu_id (self):
         return self._sheng_mu_id
@@ -75,9 +75,9 @@ class PinYinWord:
     def split (self):
         if not self.is_valid_pinyin ():
             raise Exception ("Pinyin '%s' is not a valid pinyin!" % py)
-        if self._pinyin[:2] in SHENGMU_DICT.keys ():
+        if self._pinyin[:2] in list(SHENGMU_DICT.keys ()):
             return self._pinyin[:2], self._pinyin[2:]
-        elif self._pinyin[:1] in SHENGMU_DICT.keys ():
+        elif self._pinyin[:1] in list(SHENGMU_DICT.keys ()):
             return self._pinyin[:1], self._pinyin[1:]
         else:
             return "", self._pinyin[:]
@@ -93,17 +93,17 @@ def load_pinyin_table (_file):
 
     def pinyin_table_parser (f):
         for l in f:
-            a = unicode (l, "utf-8").strip ().split ()
+            a = str (l, "utf-8").strip ().split ()
             hanzi, pinyin, freq = a
             yield (hanzi, pinyin, int (freq))
     # db.add_phrases (pinyin_table_parser (bzf))
 
     hanzi_dic = {}
     for hanzi, pinyin, freq in pinyin_table_parser (_file):
-        if not hanzi_dic.has_key (hanzi):
+        if hanzi not in hanzi_dic:
             hanzi_dic[hanzi] = {}
 
-        if hanzi_dic[hanzi].has_key (pinyin):
+        if pinyin in hanzi_dic[hanzi]:
             hanzi_dic[hanzi][pinyin] += freq
         else:
             hanzi_dic[hanzi][pinyin] = freq
@@ -113,12 +113,12 @@ def load_pinyin_table (_file):
 def load_phrase_pinyin_freq (_file):
     def phrase_pinyin_parser (f):
         for l in f:
-            phrase, pinyin, freq = unicode (l, "utf-8").strip ().split ()
-            pinyin = pinyin.replace (u"u:", u"v")
+            phrase, pinyin, freq = str (l, "utf-8").strip ().split ()
+            pinyin = pinyin.replace ("u:", "v")
             yield (phrase, pinyin, int (freq))
     phrases_dic = {}
     for phrase, pinyin, freq in phrase_pinyin_parser (_file):
-        if not phrases_dic.has_key (phrase):
+        if phrase not in phrases_dic:
             phrases_dic[phrase] = []
         phrases_dic[phrase].append ((phrase, pinyin, freq))
 
@@ -127,12 +127,12 @@ def load_phrase_pinyin_freq (_file):
 def load_phrase_pinyin (_file):
     def phrase_pinyin_parser (f):
         for l in f:
-            phrase, pinyin = unicode (l, "utf-8").strip ().split ()
-            pinyin = pinyin.replace (u"u:", u"v")
+            phrase, pinyin = str (l, "utf-8").strip ().split ()
+            pinyin = pinyin.replace ("u:", "v")
             yield (phrase, pinyin, 0)
     phrases_dic = {}
     for phrase, pinyin, freq in phrase_pinyin_parser (_file):
-        if not phrases_dic.has_key (phrase):
+        if phrase not in phrases_dic:
             phrases_dic[phrase] = []
         phrases_dic[phrase].append ((phrase, pinyin, freq))
 
@@ -142,7 +142,7 @@ def load_sogou_phrases (_file):
     import re
     dic = {}
     for l in _file:
-        w = unicode (l, "utf8")
-        w = re.split (ur"\t+", w)
+        w = str (l, "utf8")
+        w = re.split (r"\t+", w)
         dic [w[0]] = (w[0], int (w[1]))
     return dic
