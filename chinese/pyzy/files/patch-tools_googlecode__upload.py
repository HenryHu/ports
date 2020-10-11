--- tools/googlecode_upload.py.orig	2012-12-17 04:00:47 UTC
+++ tools/googlecode_upload.py
@@ -48,7 +48,7 @@
 
 __author__ = 'danderson@google.com (David Anderson)'
 
-import httplib
+import http.client
 import os.path
 import optparse
 import getpass
@@ -95,7 +95,7 @@ def upload(file, project_name, user_name, password, su
     'Content-Type': content_type,
     }
 
-  server = httplib.HTTPSConnection(upload_host)
+  server = http.client.HTTPSConnection(upload_host)
   server.request('POST', upload_uri, body, headers)
   resp = server.getresponse()
   server.close()
@@ -177,17 +177,17 @@ def upload_find_auth(file_path, project_name, summary,
       user_name = sys.stdin.readline().rstrip()
     if password is None:
       # Read password if not loaded from svn config, or on subsequent tries.
-      print 'Please enter your googlecode.com password.'
-      print '** Note that this is NOT your Gmail account password! **'
-      print 'It is the password you use to access Subversion repositories,'
-      print 'and can be found here: http://code.google.com/hosting/settings'
+      print('Please enter your googlecode.com password.')
+      print('** Note that this is NOT your Gmail account password! **')
+      print('It is the password you use to access Subversion repositories,')
+      print('and can be found here: http://code.google.com/hosting/settings')
       password = getpass.getpass()
 
     status, reason, url = upload(file_path, project_name, user_name, password,
                                  summary, labels)
     # Returns 403 Forbidden instead of 401 Unauthorized for bad
     # credentials as of 2007-07-17.
-    if status in [httplib.FORBIDDEN, httplib.UNAUTHORIZED]:
+    if status in [http.client.FORBIDDEN, http.client.UNAUTHORIZED]:
       # Rest for another try.
       user_name = password = None
       tries = tries - 1
@@ -235,12 +235,12 @@ def main():
                                          options.summary, labels,
                                          options.user, options.password)
   if url:
-    print 'The file was uploaded successfully.'
-    print 'URL: %s' % url
+    print('The file was uploaded successfully.')
+    print('URL: %s' % url)
     return 0
   else:
-    print 'An error occurred. Your file was not uploaded.'
-    print 'Google Code upload server said: %s (%s)' % (reason, status)
+    print('An error occurred. Your file was not uploaded.')
+    print('Google Code upload server said: %s (%s)' % (reason, status))
     return 1
 
 
