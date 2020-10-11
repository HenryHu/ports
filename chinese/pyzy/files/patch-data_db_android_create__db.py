--- data/db/android/create_db.py.orig	2020-10-11 19:58:39 UTC
+++ data/db/android/create_db.py
@@ -9,7 +9,7 @@ def get_sheng_yun(pinyin):
         return None, None
     if pinyin == "ng":
         return "", "en"
-    for i in xrange(2, 0, -1):
+    for i in range(2, 0, -1):
         t = pinyin[:i]
         if t in SHENGMU_DICT:
             return t, pinyin[len(t):]
@@ -17,13 +17,13 @@ def get_sheng_yun(pinyin):
 
 def read_phrases(filename):
     buf = file(filename).read()
-    buf = unicode(buf, "utf16")
+    buf = str(buf, "utf16")
     buf = buf.strip()
-    for l in buf.split(u'\n'):
-        hanzi, freq, flag, pinyin = l.split(u' ', 3)
+    for l in buf.split('\n'):
+        hanzi, freq, flag, pinyin = l.split(' ', 3)
         freq = float(freq)
         pinyin = pinyin.split()
-        if any(map(lambda c: c not in valid_hanzi, hanzi)):
+        if any([c not in valid_hanzi for c in hanzi]):
             continue
         yield hanzi, freq, pinyin
 
@@ -33,9 +33,9 @@ def create_db(filename):
     # con.execute ("PRAGMA synchronous = NORMAL;")
     # con.execute ("PRAGMA temp_store = MEMORY;")
     # con.execute ("PRAGMA default_cache_size = 5000;")
-    print "PRAGMA synchronous = NORMAL;"
-    print "PRAGMA temp_store = MEMORY;"
-    print "PRAGMA default_cache_size = 5000;"
+    print("PRAGMA synchronous = NORMAL;")
+    print("PRAGMA temp_store = MEMORY;")
+    print("PRAGMA default_cache_size = 5000;")
 
 
     sql = "CREATE TABLE py_phrase_%d (phrase TEXT, freq INTEGER, %s);"
@@ -44,7 +44,7 @@ def create_db(filename):
         for j in range(0, i + 1):
             column.append ("s%d INTEGER" % j)
             column.append ("y%d INTEGER" % j)
-        print sql % (i, ",".join(column))
+        print(sql % (i, ",".join(column)))
         # con.execute(sql % (i, column))
         # con.commit()
 
@@ -60,7 +60,7 @@ def create_db(filename):
         records_new.append((hanzi, i, pinyin))
     records_new.reverse()
     
-    print "BEGIN;"
+    print("BEGIN;")
     insert_sql = "INSERT INTO py_phrase_%d VALUES (%s);"
     for hanzi, freq, pinyin in records_new:
         columns = []
@@ -72,9 +72,9 @@ def create_db(filename):
         values = "'%s', %d, %s" % (hanzi.encode("utf8"), freq, ",".join(map(str,columns)))
             
         sql = insert_sql % (len(hanzi) - 1, values)
-        print sql
-    print "COMMIT;"
-    print "VACUUM;"
+        print(sql)
+    print("COMMIT;")
+    print("VACUUM;")
 
 def main():
     create_db(sys.argv[1])
