[app]
title = 健康记录助手
package.name = healthrecord
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
android.accept_sdk_license = True
p4a.source_dir = 
p4a.bootstrap = sdl2
p4a.android_ndk_dir = 
log_level = 2
warn_on_root = 1
[buildozer]
profile = android
