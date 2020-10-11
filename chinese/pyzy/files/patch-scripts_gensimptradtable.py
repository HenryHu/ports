--- scripts/gensimptradtable.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/gensimptradtable.py
@@ -1,11 +1,11 @@
 import sctc
-items = sctc.S_2_T.items()
+items = list(sctc.S_2_T.items())
 items.sort()
-print "const unichar simp_to_trad[][2] = {"
+print("const unichar simp_to_trad[][2] = {")
 for s, t in items:
-    print "    { 0x%x, 0x%x },   // %s => %s" % (ord(s), ord(t[0]), s.encode("utf8"), t[0].encode("utf8"))
-print "};"
+    print("    { 0x%x, 0x%x },   // %s => %s" % (ord(s), ord(t[0]), s.encode("utf8"), t[0].encode("utf8")))
+print("};")
 
-print '#define SIMP_TO_TRAD_NR (sizeof (simp_to_trad) / sizeof (simp_to_trad[0]))'
-print
+print('#define SIMP_TO_TRAD_NR (sizeof (simp_to_trad) / sizeof (simp_to_trad[0]))')
+print()
 
