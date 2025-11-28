1) بعد نجاح build (Codemagic أو محلي):
   - ستحصل على ملف: build/app/outputs/flutter-apk/app-release.apk

2) لتثبيت على جهاز أندرويد:
   - انقل الملف إلى هاتفك
   - افتح الهاتف واسمح تثبيت من مصادر غير معروفة
   - اضغط على الـ APK وثبت التطبيق

3) تشغيل محلي (لو عندك Flutter محلي):
   - flutter pub get
   - flutter build apk --release
   - أو flutter run (للتجربة)
