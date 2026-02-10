from flask import Blueprint, jsonify, request
from bson import ObjectId
from bson.errors import InvalidId

from src.config.db import get_db
from src.models.diary_model import Diary, now_utc
from src.services.diary_analysis_service import analyze_diary_content


diary_bp = Blueprint("diary", __name__)


def _serialize_diary(doc: dict) -> dict:
    """
    MongoDB의 ObjectId/Date 타입을 JSON으로 보내기 쉽게 변환합니다.
    """
    return {
        "id": str(doc.get("_id")),
        "content": doc.get("content"),
        "createdAt": doc.get("createdAt").isoformat() if doc.get("createdAt") else None,
        "analysis": doc.get("analysis"),
    }


# 1) POST /diary → 일기 저장 (+ 분석 단계)
@diary_bp.post("/")
def create_diary():
    body = request.get_json(silent=True) or {}
    content = body.get("content")

    if not content or not isinstance(content, str):
        return jsonify({"message": "content(string)는 필수입니다."}), 400

    analysis = analyze_diary_content(content)

    diary = Diary(
        content=content,
        createdAt=now_utc(),
        analysis=analysis,
    )

    db = get_db()
    result = db.diaries.insert_one(diary.to_mongo())
    saved = db.diaries.find_one({"_id": result.inserted_id})

    return jsonify(_serialize_diary(saved)), 201


# 2) GET /diary → 일기 목록 조회
@diary_bp.get("/")
def list_diaries():
    db = get_db()
    docs = db.diaries.find().sort("createdAt", -1)
    return jsonify([_serialize_diary(d) for d in docs])


# 3) DELETE /diary/:id → 일기 삭제
@diary_bp.delete("/<id>")
def delete_diary(id: str):
    try:
        oid = ObjectId(id)
    except InvalidId:
        return jsonify({"message": "유효하지 않은 id입니다."}), 400

    db = get_db()
    result = db.diaries.delete_one({"_id": oid})

    if result.deleted_count == 0:
        return jsonify({"message": "해당 일기를 찾을 수 없습니다."}), 404

    return jsonify({"message": "삭제 완료", "id": id})

