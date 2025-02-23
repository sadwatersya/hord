[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy

android.api = 34
android.ndk = 25b
android.minapi = 21
android.gradle_download = True
android.sdk_path = /home/gitpod/.buildozer/android/platform/android-sdk
# Явно указываем версии инструментов
android.ndk = 23b  # Используем более стабильную версию NDK
android.sdk = 33  # Версия SDK
android.gradle_version = 7.1.1  # Совместимая версия Gradle

# Указываем архитектуры явно
android.archs = arm64-v8a, armeabi-v7a

# Добавляем специфичные для Android настройки
android.allow_backup = False
android.enable_androidx = True
