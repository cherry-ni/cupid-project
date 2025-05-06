# frontend/config.py

import os

def get_api_base():
    """Render 환경이면 실제 URL 반환, 아니면 localhost 사용"""
    if os.getenv("RENDER") == "1":
        return "https://cupid-project.onrender.com"  # ⚠️ 실제 주소로 바꾸세요
    return "http://localhost:8000"
