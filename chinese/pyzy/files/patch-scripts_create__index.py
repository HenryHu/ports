--- scripts/create_index.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/create_index.py
@@ -6,16 +6,16 @@ con2.execute ("PRAGMA temp_store = MEMORY;")
 
 
 con2.execute("CREATE INDEX index_0_0 ON py_phrase_0(s0, y0)")
-print "py_phrase_%d done" % 0
+print("py_phrase_%d done" % 0)
 
 con2.execute("CREATE INDEX index_1_0 ON py_phrase_1(s0, y0, s1, y1)")
 con2.execute("CREATE INDEX index_1_1 ON py_phrase_1(s0, s1, y1)")
-print "py_phrase_%d done" % 1
+print("py_phrase_%d done" % 1)
 
-for i in xrange(2, 16):
+for i in range(2, 16):
 	con2.execute("CREATE INDEX index_%d_0 ON py_phrase_%d(s0, y0, s1, y1, s2, y2)" % (i, i))
 	con2.execute("CREATE INDEX index_%d_1 ON py_phrase_%d(s0, s1, s2, y2)" % (i, i))
-	print "py_phrase_%d done" % i
+	print("py_phrase_%d done" % i)
 
 # con2.execute("vacuum")
 con2.commit()
