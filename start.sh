#!/bin/bash

# 공통: .env 파일 로드
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# 백엔드 루트 기준 import를 위해 PYTHONPATH 설정
export PYTHONPATH=./backend

# 환경 확인
echo "🌍 실행 환경: ${RENDER:-local}"

# 💻 로컬 개발 환경일 경우
if [ "$RENDER" != "1" ]; then
  echo "✅ [로컬 모드] FastAPI + Streamlit 실행"

  uvicorn main:app --reload --port 8000 &
  sleep 1
  streamlit run frontend/home.py --server.port 10000
else
  echo "🚀 [배포 모드] Render에서 실행 중"

  uvicorn main:app --host 0.0.0.0 --port 8000 &
  sleep 1
  streamlit run frontend/home.py --server.port 10000 --server.address 0.0.0.0
fi
