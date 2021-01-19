--- airscan-bmp.c.orig	2021-01-19 04:38:13 UTC
+++ airscan-bmp.c
@@ -230,7 +230,7 @@ image_decoder_bmp_read_line (image_decoder *decoder, v
     int               i, wid = bmp->info_header.biWidth;
     uint8_t           *out = buffer;
 
-    if (bmp->next_line == labs(bmp->info_header.biHeight)) {
+    if ((long)bmp->next_line == labs(bmp->info_header.biHeight)) {
         return ERROR("BMP: end of file");
     }
 
