from utils import load_openai_client

# OpenAI 클라이언트 생성
client = load_openai_client()

def get_cupid_response(my_info: str, user_messages: list[str], assistant_messages: list[str]) -> str:
    # 기본 system prompt
    messages = [
        {
            "role": "system",
            "content": "너는 연애 상담 전문가이자 동성 친구야. 친근하고 일상적인 말투를 사용하지만, "
                   "단순한 응원이나 조언만 하지 말고, 상대방 입장과 본인 입장을 모두 고려한 다양한 가능성을 제시하고, "
                   "구체적인 사례를 들어 설명해주고, 현실적으로 일어날 수 있는 문제점이나 리스크도 함께 알려줘. "
        },
        {"role": "user", "content": my_info},
        {
            "role": "assistant",
            "content": "당신의 기본 정보를 확인했습니다. 연애에 대해서 어떤 것이든 물어봐!"
        },
    ]

    # 유저와 어시스턴트의 과거 대화 히스토리를 차례로 추가
    user_msgs = user_messages.copy()
    assistant_msgs = assistant_messages.copy()

    while user_msgs or assistant_msgs:
        if user_msgs:
            messages.append({"role": "user", "content": user_msgs.pop(0)})
        if assistant_msgs:
            messages.append({"role": "assistant", "content": assistant_msgs.pop(0)})

    # OpenAI 호출
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    # 응답 추출
    return response.choices[0].message.content
