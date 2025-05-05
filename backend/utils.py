# utils.py
import os
from dotenv import load_dotenv
import openai

def load_openai_client():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dotenv_path = os.path.join(current_dir, '.env')
    load_dotenv(dotenv_path=dotenv_path)

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY를 .env에서 불러올 수 없습니다.")

    return openai.OpenAI(api_key=api_key)
