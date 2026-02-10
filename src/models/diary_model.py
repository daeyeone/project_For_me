from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Optional, Dict


@dataclass
class Diary:
    """
    MongoDB는 스키마 강제가 없지만, '모델' 파일을 둬서
    데이터 형태를 팀/미래의 나에게 명확히 보여주기 위한 용도입니다.

    필드(요구사항):
    - content: string
    - createdAt: date
    - analysis: object(optional)  # 공감/요약/내일 할 일 추천 등을 담을 자리
    """

    content: str
    createdAt: datetime
    analysis: Optional[Dict[str, Any]] = None

    def to_mongo(self) -> dict:
        doc = {
            "content": self.content,
            "createdAt": self.createdAt,
        }
        if self.analysis is not None:
            doc["analysis"] = self.analysis
        return doc


def now_utc() -> datetime:
    return datetime.now(timezone.utc)

