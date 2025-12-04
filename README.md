# SmartTrading-D366

Full trading assistant (mobile + backend demo).

Contents:
- Flutter mobile app (multi-language)
- Backend demo (Flask) with /signal endpoint
- CI configs (Codemagic + GitHub Actions)
- Android embedding v2 (Kotlin MainActivity)

Build mobile:
1) flutter pub get
2) flutter build apk --release

Backend (dev):
1) cd backend
2) python -m venv venv
3) source venv/bin/activate
4) pip install -r requirements.txt
5) python app.py

Important: Do NOT commit API keys. Use environment variables or secrets.
