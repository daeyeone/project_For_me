from __future__ import annotations

from typing import Dict, Any


def analyze_diary_content(content: str) -> Dict[str, Any]:
    """
    'GPT 분석 단계'를 끼워 넣기 위한 자리입니다.

    현재는 외부 API 없이 동작해야 하므로, 아주 단순한 규칙 기반 분석을 합니다.
    나중에 GPT를 붙일 때는 이 함수 내부만 교체하면 됩니다.

    analysis 필드에 저장할 형태(요구사항):
    - empathy: 공감 메시지
    - summary: 요약
    - tomorrowTodo: 내일 할 일 추천
    """

    text = (content or "").strip()
    if not text:
        return {
            "empathy": "오늘은 어떤 하루였나요? 짧게라도 적어줘서 고마워요.",
            "summary": "내용이 비어 있어 요약할 수 없어요.",
            "tomorrowTodo": "내일은 5분만 시간을 내서 오늘 있었던 일을 한 줄로 적어보세요.",
        }

    # 규칙 기반 예시(초보자용)
    # - summary: 앞부분 일부를 잘라 간단 요약처럼 보여주기
    summary = text if len(text) <= 80 else text[:77] + "..."

    # - empathy: 감정 키워드 아주 간단히 감지
    negative_keywords = ["힘들", "불안", "우울", "짜증", "화", "슬프", "지치"]
    positive_keywords = ["좋", "행복", "기쁘", "뿌듯", "감사", "즐거"]

    empathy = "오늘도 기록해줘서 고마워요."
    if any(k in text for k in negative_keywords):
        empathy = "많이 힘들었겠어요. 그래도 이렇게 기록한 것 자체가 큰 걸음이에요."
    elif any(k in text for k in positive_keywords):
        empathy = "좋은 일이 있었나 봐요. 그 기분을 잘 간직할 수 있게 기록한 게 정말 좋아요."

    # - tomorrowTodo: 내일 할 일 추천(아주 단순 템플릿)
    tomorrow_todo = (
        "내일은 오늘의 일기에서 가장 중요했던 1가지를 골라, "
        "그걸 더 좋게 만들 수 있는 행동 1가지를 10분만 해보세요."
    )

    return {
        "empathy": empathy,
        "summary": summary,
        "tomorrowTodo": tomorrow_todo,
    }

