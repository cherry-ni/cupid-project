import streamlit as st
import requests
from sidebar import render_sidebar
import matplotlib.pyplot as plt
from config import get_api_base
from config import set_korean_font

API_BASE = get_api_base()

st.set_page_config(page_title="연애 재판관", page_icon="⚖️")
st.title("⚖️ 연애 재판관")

render_sidebar()

# 사용자로부터 상황 입력 받기
st.subheader("📌 연애 문제 상황을 설명해주세요")
situation = st.text_area("예시: 남자친구가 약속을 잊고 연락도 없이 안 나왔어요.", height=150)

# 한글 폰트 설정
set_korean_font()

def draw_judgement_bar(male_percent, female_percent):
    fig, ax = plt.subplots(figsize=(6, 1))

    # 막대 구성
    ax.barh([''], [male_percent], color='#FF6B6B', label='남자')
    ax.barh([''], [female_percent], left=[male_percent], color='#4D6AFF', label='여자')

    # 퍼센트 텍스트
    ax.text(male_percent / 2, 0, f"{male_percent}%", va='center', ha='center', color='white', fontweight='bold')
    ax.text(male_percent + female_percent / 2, 0, f"{female_percent}%", va='center', ha='center', color='white', fontweight='bold')

    # 왼쪽 오른쪽에 '남자' / '여자' 라벨 붙이기
    ax.text(-5, 0, '👨', va='center', ha='right', fontsize=12, fontweight='bold', color='#FF6B6B')
    ax.text(105, 0, '👩', va='center', ha='left', fontsize=12, fontweight='bold', color='#4D6AFF')

    ax.set_xlim(0, 100)
    ax.axis('off')

    st.pyplot(fig)


# 버튼 눌렀을 때 GPT API 호출
if st.button("🧠 GPT에게 판단 요청"):
    if not situation.strip():
        st.warning("⚠️ 먼저 상황을 입력해주세요.")
    else:
        res = requests.post(f"{API_BASE}/love_judge", json={"situation": situation})
        if res.status_code == 200:
            data = res.json()
            if "male" in data and "female" in data:
                st.write("## 💬 GPT 판단 결과")
                st.info(data.get("summary", "요약 없음"))
                draw_judgement_bar(data["male"], data["female"])
            else:
                st.error("❌ 응답 형식 오류")
                st.json(data)
        else:
            st.error("❌ 서버 오류가 발생했습니다.")
