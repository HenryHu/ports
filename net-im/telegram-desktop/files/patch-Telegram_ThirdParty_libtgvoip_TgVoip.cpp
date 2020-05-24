--- Telegram/ThirdParty/libtgvoip/TgVoip.cpp.orig	2020-05-12 12:04:12 UTC
+++ Telegram/ThirdParty/libtgvoip/TgVoip.cpp
@@ -80,7 +80,7 @@ class TgVoipImpl : public TgVoip { (public)
     TgVoipImpl(
         std::vector<TgVoipEndpoint> const &endpoints,
         TgVoipPersistentState const &persistentState,
-        std::unique_ptr<TgVoipProxy> const &proxy,
+        TgVoipProxy const *proxy,
         TgVoipConfig const &config,
         TgVoipEncryptionKey const &encryptionKey,
         TgVoipNetworkType initialNetworkType
@@ -172,6 +172,7 @@ class TgVoipImpl : public TgVoip { (public)
             config.enableAGC,
             config.enableCallUpgrade
         );
+        mappedConfig.enableVolumeControl = config.enableVolumeControl;
         mappedConfig.logFilePath = config.logPath;
         mappedConfig.statsDumpFilePath = {};
 
@@ -188,7 +189,11 @@ class TgVoipImpl : public TgVoip { (public)
         controller_->Connect();
     }
 
-    ~TgVoipImpl() override = default;
+    ~TgVoipImpl() {
+        if (controller_) {
+            stop();
+        }
+    }
 
     void setOnStateUpdated(std::function<void(TgVoipState)> onStateUpdated) override {
         onStateUpdated_ = onStateUpdated;
@@ -258,6 +263,24 @@ class TgVoipImpl : public TgVoip { (public)
         controller_->SetEchoCancellationStrength(strength);
     }
 
+    void setAudioInputDevice(std::string id) override {
+        controller_->SetCurrentAudioInput(id);
+    }
+    void setAudioOutputDevice(std::string id) override {
+        controller_->SetCurrentAudioOutput(id);
+    }
+    void setInputVolume(float level) override {
+        controller_->SetInputVolume(level);
+    }
+    void setOutputVolume(float level) override {
+        controller_->SetOutputVolume(level);
+    }
+    void setAudioOutputDuckingEnabled(bool enabled) override {
+#if defined(__APPLE__) && defined(TARGET_OS_OSX)
+        controller_->SetAudioOutputDuckingEnabled(enabled);
+#endif
+    }
+
     std::string getLastError() override {
         switch (controller_->GetLastError()) {
             case tgvoip::ERROR_INCOMPATIBLE: return "ERROR_INCOMPATIBLE";
@@ -319,7 +342,7 @@ class TgVoipImpl : public TgVoip { (public)
                     mappedState = TgVoipState::WaitInitAck;
                     break;
                 case tgvoip::STATE_ESTABLISHED:
-                    mappedState = TgVoipState::Estabilished;
+                    mappedState = TgVoipState::Established;
                     break;
                 case tgvoip::STATE_FAILED:
                     mappedState = TgVoipState::Failed;
@@ -328,7 +351,7 @@ class TgVoipImpl : public TgVoip { (public)
                     mappedState = TgVoipState::Reconnecting;
                     break;
                 default:
-                    mappedState = TgVoipState::Estabilished;
+                    mappedState = TgVoipState::Established;
                     break;
             }
 
@@ -380,11 +403,11 @@ std::string TgVoip::getVersion() {
     return tgvoip::VoIPController::GetVersion();
 }
 
-TgVoip *TgVoip::makeInstance(
+std::unique_ptr<TgVoip> TgVoip::makeInstance(
     TgVoipConfig const &config,
     TgVoipPersistentState const &persistentState,
     std::vector<TgVoipEndpoint> const &endpoints,
-    std::unique_ptr<TgVoipProxy> const &proxy,
+    TgVoipProxy const *proxy,
     TgVoipNetworkType initialNetworkType,
     TgVoipEncryptionKey const &encryptionKey
 #ifdef TGVOIP_USE_CUSTOM_CRYPTO
@@ -396,7 +419,7 @@ TgVoip *TgVoip::makeInstance(
     TgVoipAudioDataCallbacks const &audioDataCallbacks
 #endif
 ) {
-    return new TgVoipImpl(
+    return std::make_unique<TgVoipImpl>(
         endpoints,
         persistentState,
         proxy,
