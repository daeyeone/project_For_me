from flask import Flask, jsonify
from dotenv import load_dotenv
import os

from src.config.db import get_db
from src.routes.diary_routes import diary_bp


def create_app():
    load_dotenv()

    app = Flask(__name__)

    # DB 연결을 앱 시작 시 검증(실패하면 바로 에러로 알림)
    get_db()

    @app.get("/")
    def health():
        return jsonify({"ok": True})

    app.register_blueprint(diary_bp, url_prefix="/diary")

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "3000"))
    app.run(host="0.0.0.0", port=port, debug=True)

