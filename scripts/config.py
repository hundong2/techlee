"""
Daily News Generator Configuration
뉴스 생성기 설정 파일
"""

# 뉴스 주제 리스트
NEWS_TOPICS = [
    "기술 뉴스",
    "AI/머신러닝", 
    "개발자 도구",
    "프로그래밍 언어",
    "클라우드 컴퓨팅",
    "데이터 사이언스",
    "웹 개발",
    "모바일 개발",
    "오픈소스",
    "보안",
    "블록체인",
    "DevOps",
    "데이터베이스",
    "네트워킹",
    "사이버보안"
]

# Gemini API 설정
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Jekyll 설정
JEKYLL_POSTS_DIR = "../_posts"
JEKYLL_LAYOUT = "post"

# 뉴스 생성 설정
MAX_RETRIES = 3
REQUEST_TIMEOUT = 30

# 파일명 설정
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S +0900" 