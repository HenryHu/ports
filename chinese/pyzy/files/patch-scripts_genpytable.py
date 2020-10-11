--- scripts/genpytable.py.orig	2012-12-17 04:00:47 UTC
+++ scripts/genpytable.py
@@ -10,10 +10,10 @@ def str_cmp(a, b):
     else:
         return len(a) - len(b)
 
-pinyin_list = PINYIN_DICT.keys()
+pinyin_list = list(PINYIN_DICT.keys())
 pinyin_list.sort()
 
-shengmu_list = SHENGMU_DICT.keys()
+shengmu_list = list(SHENGMU_DICT.keys())
 shengmu_list.remove("")
 shengmu_list.sort()
 
@@ -243,44 +243,44 @@ def get_pinyin_with_fuzzy():
                         else:
                             bopomofo += sheng_yun_bopomofo_map[y][0]
                 else:
-                    print text
+                    print(text)
 
         yield text, bopomofo, s, y, fs1, fy1, fs2, fy2, l, flags
 
 
 def gen_header():
-    print '''/* Please do not modify this file. It is generated by script */
+    print('''/* Please do not modify this file. It is generated by script */
 #include "Types.h"
 
 namespace PY {
-'''
+''')
 
 def gen_macros():
-    print '#define PINYIN_ID_VOID    (-1)'
-    print '#define PINYIN_ID_ZERO    (0)'
+    print('#define PINYIN_ID_VOID    (-1)')
+    print('#define PINYIN_ID_ZERO    (0)')
     for y in shengmu_list:
-        print '#define PINYIN_ID_%s    (%d)' % (y.upper(), encode_pinyin(y))
+        print('#define PINYIN_ID_%s    (%d)' % (y.upper(), encode_pinyin(y)))
 
     for y in yunmu_list:
-        print '#define PINYIN_ID_%s    (%d)' % (y.upper(), encode_pinyin(y))
-    print
-    print
-    print
+        print('#define PINYIN_ID_%s    (%d)' % (y.upper(), encode_pinyin(y)))
+    print()
+    print()
+    print()
 
 def gen_option_check(name, fuzzy):
-    print '''static bool
+    print('''static bool
 %s (unsigned int option, int id, int fid)
 {
-    switch ((id << 16) | fid) {''' % name
+    switch ((id << 16) | fid) {''' % name)
     for y1, y2 in fuzzy:
         flag = "PINYIN_FUZZY_%s_%s" % (y1.upper(), y2.upper())
         args = tuple(["PINYIN_ID_%s" % y.upper() for y in [y1, y2]]) + (flag, )
-        print '''    case (%s << 16) | %s:
-        return (option & %s);''' % args
+        print('''    case (%s << 16) | %s:
+        return (option & %s);''' % args)
 
-    print '    default: return FALSE;'
-    print '    }'
-    print '}'
+    print('    default: return FALSE;')
+    print('    }')
+    print('}')
 
 def union_dups(a):
     n = {}
@@ -290,7 +290,7 @@ def union_dups(a):
         else:
             n[r[:-1]] = r[-1]
     na = []
-    for k, flags in n.items():
+    for k, flags in list(n.items()):
         na.append (tuple(list(k) + [" | ".join(flags) if flags else "0"]))
     na.sort()
     return na
@@ -300,7 +300,7 @@ def gen_table():
     pinyins = list(get_pinyin_with_fuzzy())
     pinyins = union_dups(pinyins)
 
-    print 'static const Pinyin pinyin_table[] = {'
+    print('static const Pinyin pinyin_table[] = {')
     for i, (text, bopomofo, s, y, fs1, fy1, fs2, fy2, l, flags)  in enumerate(pinyins):
         s_id = "PINYIN_ID_%s" % s.upper() if s else "PINYIN_ID_ZERO"
         y_id = "PINYIN_ID_%s" % y.upper() if y else "PINYIN_ID_ZERO"
@@ -310,7 +310,7 @@ def gen_table():
         fy2_id = "PINYIN_ID_%s" % fy2.upper() if fy2 else "PINYIN_ID_ZERO"
 
         # args = (i, ) + tuple(['"%s"' % s for s in p[:3]]) + tuple(["PINYIN_ID_%s" % s.upper() if s else "PINYIN_ID_ZERO" for s in p[3:9]]) + p[9:-1] + (str(p[-1]), )
-        print '''    {  /* %d */
+        print('''    {  /* %d */
         text        : "%s",
         bopomofo    : L"%s",
         sheng       : "%s",
@@ -318,22 +318,22 @@ def gen_table():
         pinyin_id   : {{ %s, %s }, { %s, %s }, { %s, %s }},
         len         : %d,
         flags       : %s
-    },''' % (i, text, bopomofo, s, y.replace("v", "ü"), s_id, y_id, fs1_id, fy1_id, fs2_id, fy2_id, l, flags)
+    },''' % (i, text, bopomofo, s, y.replace("v", "ü"), s_id, y_id, fs1_id, fy1_id, fs2_id, fy2_id, l, flags))
 
-    print '};'
-    print
+    print('};')
+    print()
 
     return pinyins
 
 def gen_bopomofo_table(pinyins):
     bopomofo_table = [ (i, p) for i, p in enumerate(pinyins)]
     bopomofo_table.sort(lambda a, b: cmp(a[1][1], b[1][1]))
-    print 'static const Pinyin *bopomofo_table[] = {'
+    print('static const Pinyin *bopomofo_table[] = {')
     for i, p in bopomofo_table:
         if p[1]:
-            print '    %-20s %s' % ('&pinyin_table[%d],' % i, '// "%s" => "%s"' % (p[1], p[0]))
-    print '};'
-    print
+            print('    %-20s %s' % ('&pinyin_table[%d],' % i, '// "%s" => "%s"' % (p[1], p[0])))
+    print('};')
+    print()
 
 def get_all_special(pinyins):
     for p in pinyins:
@@ -393,34 +393,34 @@ def compaired_special(pinyins):
 
 def gen_full_pinyin_table(pinyins):
     _dict = {}
-    for i in xrange(0, len(pinyins)):
+    for i in range(0, len(pinyins)):
         _dict[pinyins[i]] = i
     full_pinyin = []
-    for i in xrange(0, len(pinyins)):
+    for i in range(0, len(pinyins)):
         if pinyins[i][0] in pinyin_list:
             full_pinyin.append (pinyins[i])
     full_pinyin.sort(lambda a, b: (cmp(a[1], b[1]) << 16) + cmp(a[2],b[4]))
-    print 'static const Pinyin *full_pinyin_table[] = {'
+    print('static const Pinyin *full_pinyin_table[] = {')
     for p in full_pinyin:
-        print "    &pinyin_table[%d],    // %s" % (_dict[p], p[0])
-    print '};'
-    print
+        print("    &pinyin_table[%d],    // %s" % (_dict[p], p[0]))
+    print('};')
+    print()
 
 
 def gen_special_table(pinyins):
     _dict = {}
-    for i in xrange(0, len(pinyins)):
+    for i in range(0, len(pinyins)):
         _dict[pinyins[i][0]] = i
 
-    l = list(compaired_special(_dict.keys()))
+    l = list(compaired_special(list(_dict.keys())))
     l.sort()
-    print 'static const Pinyin *special_table[][4] = {'
+    print('static const Pinyin *special_table[][4] = {')
     for r in l:
         ids =  [("&pinyin_table[%d]," % _dict[py]).ljust(20) for py in r]
 
-        print '    { %s %s %s %s },' % tuple(ids), "/* %s %s => %s %s */" % r
-    print '};'
-    print
+        print('    { %s %s %s %s },' % tuple(ids), "/* %s %s => %s %s */" % r)
+    print('};')
+    print()
 
 
 def main():
