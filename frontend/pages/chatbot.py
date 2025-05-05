import streamlit as st
import requests
from config import get_api_base
from sidebar import render_sidebar

API_BASE = get_api_base()

st.set_page_config(page_title="Cupid 챗봇", page_icon="💬")
st.title("💬 Cupid 연애 챗봇")

render_sidebar()

# 사용자 정보 체크
if "user_info" not in st.session_state:
    st.warning("먼저 메인 페이지에서 사용자 정보를 입력해주세요!")
    st.stop()

info = st.session_state["user_info"]
my_info = f"{info['age']}세 {info['gender']}, 연애 경험 {info['experience']}, 이름: {info['name']}"

# 대화 히스토리 세션 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_started = False

# 첫 고민 입력 단계
if not st.session_state.chat_started:
    st.subheader("상담을 시작하려면 먼저 고민을 입력하세요.")
    first_question = st.text_area("당신의 연애 고민은 무엇인가요?", height=150)

    if st.button("상담 시작하기"):
        if not first_question.strip():
            st.warning("고민을 입력해주세요.")
        else:
            # 첫 요청 → 초기 질문
            response = requests.post("http://localhost:8000/chatbot", json={
                "myInfo": my_info,
                "userMessages": [first_question],
                "assistantMessages": []
            })
            if response.status_code == 200:
                assistant_reply = response.json()["assistant"]
                st.session_state.chat_history.append(("user", first_question))
                st.session_state.chat_history.append(("assistant", assistant_reply))
                st.session_state.chat_started = True
                st.rerun()
            else:
                st.error("서버 오류가 발생했습니다.")

# 채팅 화면 (상담 시작 이후)
else:
    # 과거 대화 출력
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(msg)

    # 채팅 입력창
    user_input = st.chat_input("궁금한 걸 입력하세요!")
    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        # 요청 전 대화 히스토리 분리
        user_msgs = [m for r, m in st.session_state.chat_history if r == "user"]
        assistant_msgs = [m for r, m in st.session_state.chat_history if r == "assistant"]

        user_msgs.append(user_input)

        # 요청 보내기
        response = requests.post(f"{API_BASE}/chatbot", json={
            "myInfo": my_info,
            "userMessages": user_msgs,
            "assistantMessages": assistant_msgs
        })
        if response.status_code == 200:
            assistant_reply = response.json()["assistant"]
            with st.chat_message("assistant"):
                st.markdown(assistant_reply)
            st.session_state.chat_history.append(("user", user_input))
            st.session_state.chat_history.append(("assistant", assistant_reply))
        else:
            st.error("서버 오류 발생")
