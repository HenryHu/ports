--- scripts/double.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/double.py
@@ -1,7 +1,7 @@
 import pydict
 
 for name, (sheng, yun) in pydict.SHUANGPIN_SCHEMAS:
-    print "static const char double_pinyin_%s_sheng[] = {" % name.lower()
+    print("static const char double_pinyin_%s_sheng[] = {" % name.lower())
     for c in "abcdefghijklmnopqrstuvwxyz;":
         s = sheng.get(c, "VOID")
         if s == "'":
@@ -10,10 +10,10 @@ for name, (sheng, yun) in pydict.SHUANGPIN_SCHEMAS:
             s = s.upper()
         if s == "VOID" and c in ("a", "e", "o"):
             s = "AEO"
-        print "    PINYIN_ID_%s // %s" % ((s + ",").ljust(5), c.upper())
-    print "};"
+        print("    PINYIN_ID_%s // %s" % ((s + ",").ljust(5), c.upper()))
+    print("};")
     
-    print "static const char double_pinyin_%s_yun[][2] = {" % name.lower()
+    print("static const char double_pinyin_%s_yun[][2] = {" % name.lower())
     for c in "abcdefghijklmnopqrstuvwxyz;":
         s = yun.get(c, ("VOID", "VOID"))
         if len(s) == 1:
@@ -27,14 +27,14 @@ for name, (sheng, yun) in pydict.SHUANGPIN_SCHEMAS:
             s2 = "ZERO"
         s1 = s1.upper()
         s2 = s2.upper()
-        print "    { PINYIN_ID_%s PINYIN_ID_%s }, // %s" % ((s1 + ",").ljust(5), s2.ljust(4), c.upper())
-    print "};"
+        print("    { PINYIN_ID_%s PINYIN_ID_%s }, // %s" % ((s1 + ",").ljust(5), s2.ljust(4), c.upper()))
+    print("};")
 
-print '''
+print('''
 static const struct {
     const char  (&sheng)[27];
     const char  (&yun)[27][2];
-} double_pinyin_map [] = {'''
+} double_pinyin_map [] = {''')
 for name, (sheng, yun) in pydict.SHUANGPIN_SCHEMAS:
-    print "    { double_pinyin_%s_sheng, double_pinyin_%s_yun}," %  (name.lower(), name.lower())
-print "};"
+    print("    { double_pinyin_%s_sheng, double_pinyin_%s_yun}," %  (name.lower(), name.lower()))
+print("};")
