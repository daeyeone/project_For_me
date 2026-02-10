import os
from pymongo import MongoClient
from dotenv import load_dotenv

_client = None
_db = None


def get_db():
    """
    MongoDB 연결을 한 번만 만들고 재사용합니다.
    초보자가 보기 쉽게 '연결 담당'을 이 파일에만 둡니다.
    """
    global _client, _db

    if _db is not None:
        return _db

    # app.py에서 이미 load_dotenv()를 호출하지만,
    # 테스트/스크립트에서 get_db()만 단독 호출해도 동작하도록 여기서도 보강합니다.
    load_dotenv()

    uri = os.getenv("MONGODB_URI")
    if not uri:
        raise RuntimeError("MONGODB_URI가 .env에 필요합니다.")

    _client = MongoClient(uri)

    # URI에 DB명이 있으면 그걸 쓰고, 없으면 기본 DB로 fallback
    default_db = _client.get_default_database()
    _db = default_db if default_db is not None else _client["diary_db"]

    # 연결 확인용 ping
    # - 로컬 MongoDB가 꺼져있다면 여기서 에러가 납니다.
    # - Atlas를 쓰면 MONGODB_URI를 Atlas 연결 문자열로 바꾸면 됩니다.
    _db.command("ping")

    return _db

