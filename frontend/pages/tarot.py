import streamlit as st
from PIL import Image
import random
import os
import requests
from config import get_api_base
from sidebar import render_sidebar

# Streamlit 설정
st.set_page_config(page_title="타로 카드 리딩", page_icon="🔮")
st.title("🔮 타로 카드 리딩")

render_sidebar()

# 카드 이름 → 파일명 매핑 (전체 카드 반영)
TAROT_CARDS = {
    "The Fool": "the_fool.png",
    "The Magician": "the_magician.png",
    "The High Priestess": "the_high_priestess.png",
    "The Empress": "the_empress.png",
    "The Emperor": "the_emperor.png",
    "The Hierophant": "the_hierophant.png",
    "The Lovers": "the_lovers.png",
    "The Chariot": "the_chariot.png",
    "Strength": "strength.png",
    "The Hermit": "the_hermit.png",
    "Wheel of Fortune": "wheel_of_fortune.png",
    "Justice": "justice.png",
    "The Hanged Man": "the_hanged_man.png",
    "Death": "death.png",
    "Temperance": "temperance.png",
    "The Devil": "the_devil.png",
    "The Tower": "the_tower.png",
    "The Star": "the_star.png",
    "The Moon": "the_moon.png",
    "The Sun": "the_sun.png",
    "Judgement": "judgement.png",
    "The World": "the_world.png",
    "Ace of Cups": "ace_of_cups.png",
    "Two of Cups": "two_of_cups.png",
    "Three of Cups": "three_of_cups.png",
    "Four of Cups": "four_of_cups.png",
    "Five of Cups": "five_of_cups.png",
    "Six of Cups": "six_of_cups.png",
    "Seven of Cups": "seven_of_cups.png",
    "Eight of Cups": "eight_of_cups.png",
    "Nine of Cups": "nine_of_cups.png",
    "Ten of Cups": "ten_of_cups.png",
    "Page of Cups": "page_of_cups.png",
    "Knight of Cups": "knight_of_cups.png",
    "Queen of Cups": "queen_of_cups.png",
    "King of Cups": "king_of_cups.png",
    "Ace of Pentacles": "ace_of_pentacles.png",
    "Two of Pentacles": "two_of_pentacles.png",
    "Three of Pentacles": "three_of_pentacles.png",
    "Four of Pentacles": "four_of_pentacles.png",
    "Five of Pentacles": "five_of_pentacles.png",
    "Six of Pentacles": "six_of_pentacles.png",
    "Seven of Pentacles": "seven_of_pentacles.png",
    "Eight of Pentacles": "eight_of_pentacles.png",
    "Nine of Pentacles": "nine_of_pentacles.png",
    "Ten of Pentacles": "ten_of_pentacles.png",
    "Page of Pentacles": "page_of_pentacles.png",
    "Knight of Pentacles": "knight_of_pentacles.png",
    "Queen of Pentacles": "queen_of_pentacles.png",
    "King of Pentacles": "king_of_pentacles.png",
    "Ace of Swords": "ace_of_swords.png",
    "Two of Swords": "two_of_swords.png",
    "Three of Swords": "three_of_swords.png",
    "Four of Swords": "four_of_swords.png",
    "Five of Swords": "five_of_swords.png",
    "Six of Swords": "six_of_swords.png",
    "Seven of Swords": "seven_of_swords.png",
    "Eight of Swords": "eight_of_swords.png",
    "Nine of Swords": "nine_of_swords.png",
    "Ten of Swords": "ten_of_swords.png",
    "Page of Swords": "page_of_swords.png",
    "Knight of Swords": "knight_of_swords.png",
    "Queen of Swords": "queen_of_swords.png",
    "King of Swords": "king_of_swords.png",
    "Ace of Wands": "ace_of_wands.png",
    "Two of Wands": "two_of_wands.png",
    "Three of Wands": "three_of_wands.png",
    "Four of Wands": "four_of_wands.png",
    "Five of Wands": "five_of_wands.png",
    "Six of Wands": "six_of_wands.png",
    "Seven of Wands": "seven_of_wands.png",
    "Eight of Wands": "eight_of_wands.png",
    "Nine of Wands": "nine_of_wands.png",
    "Ten of Wands": "ten_of_wands.png",
    "Page of Wands": "page_of_wands.png",
    "Knight of Wands": "knight_of_wands.png",
    "Queen of Wands": "queen_of_wands.png",
    "King of Wands": "king_of_wands.png"
}

API_BASE = get_api_base()

# 절대 경로로 이미지 폴더 지정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_PATH = os.path.join(BASE_DIR, "..", "assets", "tarot")

# 질문 입력
question = st.text_input("💬 당신의 연애 고민은 무엇인가요?")
can_select_cards = question.strip() != ""

# 카드 섞기
if "random_cards" not in st.session_state:
    st.session_state.random_cards = random.sample(list(TAROT_CARDS.items()), 9)

if "selected_cards" not in st.session_state:
    st.session_state.selected_cards = []

# 카드 선택 UI
# 카드 선택 UI
st.subheader("9장의 카드 중 3장을 선택하세요")
cols = st.columns(3)
for i, (card_name, file_name) in enumerate(st.session_state.random_cards):
    with cols[i % 3]:
        img_path = os.path.join(ASSET_PATH, file_name)
        img = Image.open(img_path)
        st.image(img, caption=card_name, use_container_width=True)

        if not question.strip():
            continue  # ❗ 질문 없으면 버튼은 아예 렌더링하지 않음

        selected = card_name in st.session_state.selected_cards
        can_select_more = len(st.session_state.selected_cards) < 3

        if selected:
            st.button("✅ 선택됨", key=f"{card_name}_chosen", disabled=True)
        elif can_select_more:
            if st.button(f"선택: {card_name}", key=f"{card_name}_choose"):
                st.session_state.selected_cards.append(card_name)
                st.rerun()
        else:
            st.button("선택", key=f"{card_name}_disabled", disabled=True)

# 선택한 카드 표시
if st.session_state.selected_cards:
    st.write("### 🃏 선택한 카드")
    st.write(", ".join(st.session_state.selected_cards))

# 해석 요청
if len(st.session_state.selected_cards) == 3 and question.strip():
    if st.button("🔍 해석 요청하기"):
        with st.spinner("GPT가 해석 중..."):
            res = requests.post(f"{API_BASE}/tarot", json={
                "user_question": question,
                "selected_cards": st.session_state.selected_cards
            })
            if res.status_code == 200:
                st.write("## 💡 타로 해석 결과")
                st.markdown(res.json()["reading"])
            else:
                st.error("서버 응답 오류가 발생했습니다.")
