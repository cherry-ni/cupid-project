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

  # FastAPI는 내부 백엔드 서버로 8000번 포트에서 실행 (외부 노출되지 않음)
  uvicorn main:app --host 0.0.0.0 --port 8000 &

  # Streamlit은 외부에 노출되도록 Render에서 지정한 포트에 맞춰 실행
  sleep 1
  streamlit run frontend/home.py \
    --server.port $PORT \
    --server.address 0.0.0.0 \
    --server.headless true \
    --browser.gatherUsageStats false
fi
