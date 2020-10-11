--- scripts/addheader.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/addheader.py
@@ -6,13 +6,13 @@ def add_header(name, header):
         lines = fin.readlines()
     with file(name, "w") as fout:
         for l in header:
-            print >> fout, l,
+            print(l, end=' ', file=fout)
         if lines[0].startswith("/*") and lines[0].endswith("*/\n"):
             pass
         else:
-            print >> fout, lines[0],
+            print(lines[0], end=' ', file=fout)
         for l in lines[1:]:
-            print >> fout, l,
+            print(l, end=' ', file=fout)
 
 def main():
     with file("header") as f:
