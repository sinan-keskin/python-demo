# app.py
# Basit "Hello, World!" uygulaması 💬

# 1️⃣ Terminal çıktısı
def main():
    print("Hello, World! 👋")


# 2️⃣ Flask ile mini web sunucusu (isteğe bağlı)
try:
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World! 🌍 (from Flask)"
except ImportError:
    app = None


if __name__ == "__main__":
    main()
    if app:
        print("🌐 Flask server çalışıyor: http://127.0.0.1:5000")
        app.run(debug=True)
