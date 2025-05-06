# frontend/config.py

import os

def get_api_base():
    """Render 배포 환경에서는 외부 PORT가 1개만 허용되므로 localhost 사용"""
    if os.getenv("RENDER") == "1":
        return "http://localhost:8000"
    return "http://localhost:8000"
