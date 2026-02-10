# project_For_me
하루의 끝을 정리하는 데 도움을 주는 간단한 일기 API 서버입니다.

## 개요
Python + Flask + MongoDB로 만든 **백엔드 전용 일기 서비스**입니다.

- 사용자가 일기를 작성하면 저장하면서 동시에 **분석 단계**를 거칩니다.
- 분석 결과는 `analysis` 필드에 아래 구조로 저장됩니다.
  - `empathy`: 공감 메시지
  - `summary`: 일기 내용 요약
  - `tomorrowTodo`: 내일 할 일 추천

### 제공 API
- **POST** `/diary`  
  - 요청: `{ "content": "오늘 하루에 대한 일기 내용" }`
  - 동작: 일기 저장 + 분석 결과 생성 후 `analysis` 필드에 함께 저장
- **GET** `/diary`  
  - 동작: 저장된 일기 목록 조회 (최신 순)
- **DELETE** `/diary/:id`  
  - 동작: 특정 일기 삭제

## 폴더 구조
```text
project_For_me/
├─ app.py                    # Flask 앱 엔트리 포인트
├─ requirements.txt          # Python 패키지 의존성
├─ .env                      # 환경변수 (PORT, MONGODB_URI 등)
└─ src/
   ├─ config/db.py           # MongoDB 연결 전담
   ├─ models/diary_model.py  # Diary 데이터 모델 정의
   ├─ services/
   │  └─ diary_analysis_service.py  # 일기 분석 로직 (나중에 GPT로 교체 예정)
   └─ routes/diary_routes.py # /diary 관련 라우터 (API 엔드포인트)
```

## 실행 방법
### 1) 가상환경 생성 및 패키지 설치
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2) 환경변수 설정
프로젝트 루트에 `.env` 파일을 생성/수정합니다.

```env
PORT=3000
MONGODB_URI=mongodb://127.0.0.1:27017/diary_db
```

> 로컬 MongoDB를 사용하지 않고 MongoDB Atlas를 쓸 경우,  
> `MONGODB_URI` 값을 Atlas에서 제공하는 연결 문자열로 교체하면 됩니다.

### 3) 서버 실행
```bash
python app.py
```

이후 브라우저 또는 API 툴(Postman, curl 등)에서 `http://localhost:3000/diary`로 요청을 보낼 수 있습니다.
