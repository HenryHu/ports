--- Telegram/ThirdParty/libtgvoip/threading.h.orig	2018-07-17 16:48:21 UTC
+++ Telegram/ThirdParty/libtgvoip/threading.h
@@ -42,6 +42,9 @@ namespace tgvoip{
 #ifdef __APPLE__
 #include "os/darwin/DarwinSpecific.h"
 #endif
+#ifdef __FreeBSD__
+#include <pthread_np.h>
+#endif
 
 namespace tgvoip{
 	class Mutex{
@@ -115,7 +118,9 @@ namespace tgvoip{
 		static void* ActualEntryPoint(void* arg){
 			Thread* self=reinterpret_cast<Thread*>(arg);
 			if(self->name){
-#if !defined(__APPLE__) && !defined(__gnu_hurd__)
+#if defined(__FreeBSD__)
+				pthread_set_name_np(self->thread, self->name);
+#elif !defined(__APPLE__) && !defined(__gnu_hurd__)
 				pthread_setname_np(self->thread, self->name);
 #elif !defined(__gnu_hurd__)
 				pthread_setname_np(self->name);
