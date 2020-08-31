--- tg_owt/src/rtc_base/units/unit_base.h.orig	2020-08-30 09:41:57 UTC
+++ tg_owt/src/rtc_base/units/unit_base.h
@@ -53,9 +53,6 @@ class UnitBase {
   constexpr bool operator==(const Unit_T& other) const {
     return value_ == other.value_;
   }
-  constexpr bool operator!=(const Unit_T& other) const {
-    return value_ != other.value_;
-  }
   constexpr bool operator<=(const Unit_T& other) const {
     return value_ <= other.value_;
   }
