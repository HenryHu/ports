--- scripts/create_unique_index.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/create_unique_index.py
@@ -6,22 +6,22 @@ con2.execute ("PRAGMA temp_store = MEMORY;")
 
 
 con2.execute("CREATE UNIQUE INDEX IF NOT EXISTS index_0_0 ON py_phrase_0(s0, y0, phrase)")
-print "py_phrase_%d done" % 0
+print("py_phrase_%d done" % 0)
 
 con2.execute("CREATE UNIQUE INDEX IF NOT EXISTS index_1_0 ON py_phrase_1(s0, y0, s1, y1, phrase)")
 con2.execute("CREATE INDEX IF NOT EXISTS index_1_1 ON py_phrase_1(s0, s1, y1)")
-print "py_phrase_%d done" % 1
+print("py_phrase_%d done" % 1)
 
-for i in xrange(2, 16):
+for i in range(2, 16):
     sql = "CREATE UNIQUE INDEX IF NOT EXISTS index_%d_0 ON py_phrase_%d (" % (i, i)
     sql = sql + "s0,y0"
-    for j in xrange(1, i + 1):
+    for j in range(1, i + 1):
         sql = sql + ",s%d,y%d" % (j, j)
     sql = sql + ", phrase)"
-    print sql
+    print(sql)
     con2.execute(sql)
     con2.execute("CREATE INDEX IF NOT EXISTS index_%d_1 ON py_phrase_%d(s0, s1, s2, y2)" % (i, i))
-    print "py_phrase_%d done" % i
+    print("py_phrase_%d done" % i)
 
 # con2.execute("vacuum")
 con2.commit()
