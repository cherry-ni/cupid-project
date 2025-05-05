# 1. 어떤 OS/언어 환경으로 시작할지
FROM python:3.9-slim

# 2. 작업 폴더 설정
WORKDIR /app

# 3. 의존성 파일 복사
COPY requirements.txt .

# 4. 필요한 파이썬 패키지 설치
RUN pip install -r requirements.txt

# 5. 전체 소스 코드 복사 (backend + frontend)
COPY . .

# 6. 실행할 명령어 지정
CMD ["bash", "start.sh"]