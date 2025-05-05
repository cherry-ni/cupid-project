from backend.utils import load_openai_client

# OpenAI 클라이언트 생성
client = load_openai_client()

import json

def get_judgement_result(situation: str) -> dict:
    prompt = (
        "너는 공정한 연애 토론 심판관이야. 다음 연애 상황에서 남자와 여자가 각각 얼마나 잘못했는지 수치로 판단해줘.\n"
        "- 응답 형식은 JSON으로 정확히 지켜줘.\n"
        "- 예시: {\"male\": 55, \"female\": 45, \"summary\": \"남자가 더 큰 책임이 있어 보입니다.\"}\n"
        "- 퍼센트 합은 반드시 100이 되게 해.\n"
        "- 'json'이라는 말 없이 JSON 객체만 응답해줘.\n"
        "그리고 summary에 들어갈 내용은 그렇게 판단한 이유에 대해서 자세한 판단 근거를 1. 2... 이런 식으로 제시해줘. 줄바꿈도 포함해야 한다."
        f"상황: {situation}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()

    # "json"이라는 단어가 앞에 붙어도 파싱할 수 있게 정리
    if content.lower().startswith("json"):
        content = content[4:].strip()

    try:
        return json.loads(content)
    except Exception:
        return {
            "error": "GPT 응답 파싱 실패",
            "raw_response": content
        }
