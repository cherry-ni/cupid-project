#!/bin/bash

# FastAPI 백엔드 실행 (백그라운드)
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Streamlit 프론트 실행 (Render는 포트 10000 하나만 외부에 노출 가능)
streamlit run frontend/home.py --server.port 10000 --server.address 0.0.0.0