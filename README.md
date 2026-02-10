# project_For_me
AI agent that helps you wrap up your day

## What this is
Simple diary API server (Python + Flask + MongoDB).

Required APIs:
- POST `/diary` : create diary (includes analysis step)
- GET `/diary` : list diaries
- DELETE `/diary/:id` : delete diary

## Folder structure
```text
project_For_me/
├─ app.py
├─ requirements.txt
├─ .env
└─ src/
   ├─ config/db.py
   ├─ models/diary_model.py
   ├─ services/diary_analysis_service.py
   └─ routes/diary_routes.py
```

## Run
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
