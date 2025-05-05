from backend.utils import load_openai_client

# OpenAI 클라이언트 생성
client = load_openai_client()

# 전체 타로 카드 목록
ALL_TAROT_CARDS = [
    "The Fool", "The Magician", "The High Priestess", "The Empress",
    "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
    "Strength", "The Hermit", "Wheel of Fortune", "Justice",
    "The Hanged Man", "Death", "Temperance", "The Devil",
    "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World", "Ace of Cups", "Two of Cups",
    "Three of Cups", "Four of Cups", "Five of Cups", "Six of Cups",
    "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups",
    "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups",
    "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles",
    "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles",
    "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles",
    "Queen of Pentacles", "King of Pentacles", "Ace of Swords", "Two of Swords",
    "Three of Swords", "Four of Swords", "Five of Swords", "Six of Swords",
    "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords",
    "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords",
    "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands",
    "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands",
    "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands",
    "Queen of Wands", "King of Wands"
]

def get_tarot_reading(user_question: str, selected_cards: list[str]) -> str:
    card_names = ", ".join(selected_cards)
    messages = [
        {"role": "system", "content": "너는 최고의 타로 전문가야. 질문과 선택된 타로 카드 3장을 해석해줘."},
        {"role": "user", "content": f"질문: {user_question}\n선택한 카드: {card_names}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content
