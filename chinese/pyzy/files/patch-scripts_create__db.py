--- scripts/create_db.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/create_db.py
@@ -25,7 +25,7 @@ def get_sheng_yun(pinyin):
 		return None, None
 	if pinyin == "ng":
 		return "", "en"
-	for i in xrange(2, 0, -1):
+	for i in range(2, 0, -1):
 		t = pinyin[:i]
 		if t in SHENGMU_DICT:
 			return t, pinyin[len(t):]
@@ -45,7 +45,7 @@ con2.commit()
 new_freq = 0
 freq = 0
 
-print "INSERTING"
+print("INSERTING")
 for  r in con1.execute("SELECT * FROM py_phrase ORDER BY freq"):
 	ylen = r[0]
 	phrase = r[10]
@@ -54,9 +54,9 @@ for  r in con1.execute("SELECT * FROM py_phrase ORDER 
 		new_freq += 1
 
 	if ylen <= 4:
-		pys = map(lambda id: ID_PINYIN_DICT[id], r[1: 1 + ylen])
+		pys = [ID_PINYIN_DICT[id] for id in r[1: 1 + ylen]]
 	else:
-		pys = map(lambda id: ID_PINYIN_DICT[id], r[1: 5]) + r[5].encode("utf8").split("'")
+		pys = [ID_PINYIN_DICT[id] for id in r[1: 5]] + r[5].encode("utf8").split("'")
 
 	i = ylen - 1
 	if i >= 15:
@@ -70,17 +70,17 @@ for  r in con1.execute("SELECT * FROM py_phrase ORDER 
 		sheng_yun.append(y)
 	
 	
-	column = [phrase, new_freq] + map(encode_pinyin, sheng_yun)
+	column = [phrase, new_freq] + list(map(encode_pinyin, sheng_yun))
 
 	sql = insert_sql % (i, ",".join(["?"] * len(column)))
 	con2.execute (sql, column)
 
-print "Remove duplicate"
-for i in xrange(0, 16):
-    sql = "DELETE FROM py_phrase_%d WHERE rowid IN (SELECT rowid FROM (SELECT count() as count, rowid FROM py_phrase_%d GROUP by %s,phrase) WHERE count > 1)" % (i, i, ",".join(map(lambda i: "s%d,y%d"%(i,i), range(0, i + 1))))
+print("Remove duplicate")
+for i in range(0, 16):
+    sql = "DELETE FROM py_phrase_%d WHERE rowid IN (SELECT rowid FROM (SELECT count() as count, rowid FROM py_phrase_%d GROUP by %s,phrase) WHERE count > 1)" % (i, i, ",".join(["s%d,y%d"%(i,i) for i in range(0, i + 1)]))
     con2.execute(sql)
 con2.commit()
-print "CACUUM"
+print("CACUUM")
 con2.execute("VACUUM;")
 con2.commit()
 
