--- src/lottie/lottiemodel.cpp.orig	2020-10-26 02:07:10 UTC
+++ src/lottie/lottiemodel.cpp
@@ -188,11 +188,11 @@ void LOTGradient::populate(VGradientStops &stops, int 
         return;
     }
     int            colorPoints = mColorPoints;
-    if (colorPoints < 0 || colorPoints > size / 4) {  // for legacy bodymovin (ref: lottie-android)
+    if (colorPoints < 0 || colorPoints > (int)size / 4) {  // for legacy bodymovin (ref: lottie-android)
         colorPoints = int(size / 4);
     }
     auto    opacityArraySize = size - colorPoints * 4;
-    if ((opacityArraySize % 2 != 0) || (colorPoints > opacityArraySize / 2 && opacityArraySize < 4)) {
+    if ((opacityArraySize % 2 != 0) || (colorPoints > (int)opacityArraySize / 2 && opacityArraySize < 4)) {
         opacityArraySize = 0;
     }
     float *opacityPtr = ptr + (colorPoints * 4);
