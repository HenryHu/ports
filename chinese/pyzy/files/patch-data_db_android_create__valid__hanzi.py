--- data/db/android/create_valid_hanzi.py.orig	2012-12-17 04:00:47 UTC
+++ data/db/android/create_valid_hanzi.py
@@ -7,11 +7,11 @@ def main():
     hanzi = get_validate_hanzi()
     hanzi = list(hanzi)
     hanzi.sort()
-    print "# -*- coding: utf-8 -*- "
-    print "valid_hanzi = set(["
+    print("# -*- coding: utf-8 -*- ")
+    print("valid_hanzi = set([")
     for c in hanzi:
-        print "    u\"%s\"," % c.encode("utf8")
-    print "])"
+        print("    u\"%s\"," % c.encode("utf8"))
+    print("])")
 
 if __name__ == "__main__":
     main()
