--- Telegram/ThirdParty/libtgvoip/webrtc_dsp/absl/meta/type_traits.h.orig	2020-05-12 12:04:12 UTC
+++ Telegram/ThirdParty/libtgvoip/webrtc_dsp/absl/meta/type_traits.h
@@ -410,7 +410,7 @@ template <typename T>
 using underlying_type_t = typename std::underlying_type<T>::type;
 
 template <typename T>
-using result_of_t = typename std::result_of<T>::type;
+using result_of_t = typename std::invoke_result<T>::type;
 
 namespace type_traits_internal {
 template <typename Key, typename = size_t>
