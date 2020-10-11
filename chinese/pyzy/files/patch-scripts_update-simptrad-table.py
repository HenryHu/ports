--- scripts/update-simptrad-table.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/update-simptrad-table.py
@@ -6,7 +6,7 @@ from ZhConversion import *
 from valid_hanzi import *
 
 def convert(s, d, n):
-    out = u""
+    out = ""
     end = len(s)
     begin = 0
     while begin < end:
@@ -20,9 +20,9 @@ def convert(s, d, n):
     return out
 
 def filter_more(records, n):
-    han = filter(lambda (k, v): len(k) <= n, records)
+    han = [k_v1 for k_v1 in records if len(k_v1[0]) <= n]
     hand = dict(han)
-    hanm = filter(lambda (k, v): convert(k, hand, n) != v, records)
+    hanm = [k_v2 for k_v2 in records if convert(k_v2[0], hand, n) != k_v2[1]]
     return hanm + han
 
 def filter_func(args):
@@ -46,24 +46,24 @@ def filter_func(args):
     return True
 
 def get_records():
-    records = zh2Hant.items()
+    records = list(zh2Hant.items())
 
-    records = filter(filter_func, records)
+    records = list(filter(filter_func, records))
 
-    maxlen = max(map(lambda (k,v): len(k), records))
+    maxlen = max([len(k_v[0]) for k_v in records])
     for i in range(1,  maxlen - 1):
         records = filter_more(records, i)
-    records = map(lambda (k, v): (k.encode("utf8"), v.encode("utf8")), records)
+    records = [(k_v3[0].encode("utf8"), k_v3[1].encode("utf8")) for k_v3 in records]
     records.sort()
     return maxlen, records
 
 def main():
-    print "static const char *simp_to_trad[][2] = {"
+    print("static const char *simp_to_trad[][2] = {")
     maxlen, records = get_records()
     for s, ts in records:
-        print '    { "%s", "%s" },' % (s, ts)
-    print "};"
-    print '#define SIMP_TO_TRAD_MAX_LEN (%d)' % maxlen
+        print('    { "%s", "%s" },' % (s, ts))
+    print("};")
+    print('#define SIMP_TO_TRAD_MAX_LEN (%d)' % maxlen)
 
 if __name__ == "__main__":
     main()
