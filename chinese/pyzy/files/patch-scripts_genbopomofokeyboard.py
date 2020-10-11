--- scripts/genbopomofokeyboard.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/genbopomofokeyboard.py
@@ -80,10 +80,10 @@ def tochar(ch):
 
 def gen_table():
     i = 0
-    print 'static const unsigned char'
-    print 'bopomofo_keyboard[][41][2] = {'
+    print('static const unsigned char')
+    print('bopomofo_keyboard[][41][2] = {')
     for keyboard in bopomofo_keyboard:
-        print '    {'
+        print('    {')
         items = []
         i=1
         for v in keyboard:
@@ -91,10 +91,10 @@ def gen_table():
             i += 1
         items.sort()
         for k,v in items:
-            print '        { %-4s, %-15s },' % (tochar(k),v)
-        print '    },'
-    print '};'
-    print
+            print('        { %-4s, %-15s },' % (tochar(k),v))
+        print('    },')
+    print('};')
+    print()
 
 if __name__ == "__main__":
     gen_table()
