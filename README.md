# 💘 Cupid Project: 연애 상담 AI 웹서비스

GPT API와 Streamlit, FastAPI, Docker, Render를 활용한 **AI 기반 연애 상담 웹 애플리케이션**입니다.  
연애 고민부터 타로 해석, 연애 상황 판단까지 — 연애에 관한 모든 문제를 AI가 함께 해결해드립니다.

---

## 📌 주요 기능

### 1. 💬 연애 챗봇 (Cupid)

- GPT-4o API를 활용한 **연애 전문 AI 챗봇**
- 사용자의 기본 정보를 바탕으로 친근하고 현실적인 조언 제공
- 대화 히스토리를 기억하여 자연스러운 대화 유지

### 2. 🔮 연애 타로 리딩

- 질문을 입력하고 3장의 타로 카드를 선택하면 GPT가 **타로 리딩 결과 해석**
- 78장의 타로 카드 중 9장이 랜덤으로 제공

### 3. ⚖️ 연애 재판관 (Love Judge)

- 연애 상황을 입력하면 GPT가 남자/여자 **누가 더 잘못했는지 퍼센트로 판단**
- 판단 근거와 함께 시각적인 막대그래프로 결과 출력

---

## 🛠️ 개발 환경 및 스택

| 항목 | 기술 |
|------|------|
| 프론트엔드 | Streamlit |
| 백엔드 | FastAPI |
| AI 모델 | OpenAI GPT-4o API |
| 환경 구성 | Python 3.9, Docker, Bash |
| 배포 | Render (Docker 기반 배포) |

---

## 🚀 실행 방법

### ✅ 로컬 실행
```bash
# 1. 가상환경 생성 및 활성화
python3 -m venv .venv
source .venv/bin/activate

# 2. 의존성 설치
pip install -r requirements.txt

# 3. API 연결
.env 파일에 API_KEY=your_API_KEY 추가

# 4. 서버 실행
bash start.sh
```

### ✅ 배포 
[cupid-project link](cupid-project.onrender.com)