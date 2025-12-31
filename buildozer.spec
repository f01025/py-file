[app]
title = M42 Tool
package.name = m42helper
icon.filename = assets/icon.png
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,kv,atlas,json
version = 0.1

# We stick to these stable versions
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow

orientation = portrait
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.skip_update = False
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
