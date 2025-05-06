from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.chat_service import get_cupid_response
from services.tarot_service import get_tarot_reading
from services.judge_service import get_judgement_result

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 중에는 *로 열어둬도 OK
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 데이터 모델
class ChatRequest(BaseModel):
    myInfo: str
    userMessages: list[str]
    assistantMessages: list[str]

class TarotRequest(BaseModel):
    user_question: str
    selected_cards: list[str]

class DebateRequest(BaseModel):
    situation: str

@app.post("/chatbot")
async def chat_with_cupid(request: ChatRequest):
    try:
        # 비즈니스 로직을 service로 위임
        cupid_response = get_cupid_response(
            my_info=request.myInfo,
            user_messages=request.userMessages,
            assistant_messages=request.assistantMessages,
        )
        return {"assistant": cupid_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tarot")
async def tarot_reading(request: TarotRequest):
    try:
        # 비즈니스 로직을 service로 위임
        tarot_response = get_tarot_reading(
            user_question=request.user_question,
            selected_cards=request.selected_cards
        )
        return {"reading": tarot_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/love_judge")
async def debate(request: DebateRequest):
    try:
        return get_judgement_result(request.situation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))