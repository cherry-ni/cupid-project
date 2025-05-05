import streamlit as st
from sidebar import render_sidebar

# 페이지 기본 설정
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 메인 페이지")
st.subheader("1. 당신의 기본 정보를 입력해주세요")

render_sidebar()

name = st.text_input("이름")
age = st.text_input("나이")
gender = st.selectbox("성별", ["여성", "남성", "기타"])
experience = st.selectbox("연애 경험 횟수", ["0회", "1~2회", "3~5회", "5회 이상"])

if st.button("정보 저장하기"):
    if not all([name.strip(), age.strip(), gender, experience]):
        st.warning("모든 항목을 입력해야 합니다.")
    else:
        st.session_state["user_info"] = {
            "name": name,
            "age": age,
            "gender": gender,
            "experience": experience
        }
        st.success("✅ 정보가 저장되었습니다. 원하는 메뉴를 선택하세요!")

# 페이지 이동 버튼
if st.button("💘 연애 상담이 필요하다면? 내가 들어줄게!"):
    st.switch_page("pages/chatbot.py")  # chatbot.py로 이동

if st.button("🔮 연애 고민이 있다면? 타로를 보는 건 어때!"):
    st.switch_page("pages/tarot.py")  # tarot.py로 이동

if st.button("👩‍⚖️ 누가 잘못했는지 모르겠다면? 내가 판단해줄게!"):
    st.switch_page("pages/love_judge.py")  # love_judge.py로 이동