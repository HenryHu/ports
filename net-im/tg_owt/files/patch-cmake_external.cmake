--- cmake/external.cmake.orig	2021-09-15 08:38:11 UTC
+++ cmake/external.cmake
@@ -114,6 +114,7 @@ function(link_libabsl target_name)
         set(absl_FOUND ${absl_FOUND} PARENT_SCOPE)
         if (absl_FOUND)
             target_link_libraries(${target_name} INTERFACE absl::strings)
+            target_include_directories(${target_name} PRIVATE $<TARGET_PROPERTY:absl::strings,INTERFACE_INCLUDE_DIRECTORIES>)
         endif()
     endif()
     if (NOT absl_FOUND)
