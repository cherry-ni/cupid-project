import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

def get_api_base():
    """Render 배포 환경에서는 외부 PORT가 1개만 허용되므로 localhost 사용"""
    if os.getenv("RENDER") == "1":
        return "http://localhost:8000"
    return "http://localhost:8000"

def set_korean_font():
    # Render에서 설치된 NanumGothic 사용
    for font in fm.findSystemFonts():
        if 'NanumGothic' in font:
            plt.rcParams['font.family'] = 'NanumGothic'
            return
    # macOS용 fallback
    if os.name == 'posix':
        plt.rcParams['font.family'] = 'AppleGothic'  # macOS용
    else:
        plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows용
