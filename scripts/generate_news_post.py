#!/usr/bin/env python3
"""
Daily News Post Generator using Gemini API
매일 정해진 시간에 특정 주제의 뉴스를 생성하여 Jekyll 블로그 포스트로 만드는 스크립트
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
import random
from pathlib import Path

# 설정 파일 import
from config import (
    NEWS_TOPICS, 
    GEMINI_API_URL, 
    JEKYLL_POSTS_DIR, 
    JEKYLL_LAYOUT,
    MAX_RETRIES,
    REQUEST_TIMEOUT,
    DATE_FORMAT,
    TIME_FORMAT
)

# Gemini API 설정
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def get_gemini_response(prompt):
    """Gemini API를 사용해서 응답을 받아옵니다."""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
    
    headers = {
        "Content-Type": "application/json",
    }
    
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
    
    url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"
    
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                return result['candidates'][0]['content']['parts'][0]['text']
            else:
                raise Exception("Gemini API 응답에서 텍스트를 찾을 수 없습니다.")
                
        except requests.exceptions.RequestException as e:
            print(f"API 요청 오류 (시도 {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt == MAX_RETRIES - 1:
                return None
        except Exception as e:
            print(f"응답 처리 오류 (시도 {attempt + 1}/{MAX_RETRIES}): {e}")
            if attempt == MAX_RETRIES - 1:
                return None
    
    return None

def generate_news_content(topic):
    """특정 주제에 대한 뉴스 내용을 생성합니다."""
    
    prompt = f"""
다음 주제에 대한 오늘의 기술 뉴스를 한국어로 작성해주세요: {topic}

다음 형식으로 작성해주세요:

## 제목
간결하고 매력적인 제목

## 요약
2-3문장으로 핵심 내용 요약

## 주요 내용
- 첫 번째 주요 포인트
- 두 번째 주요 포인트  
- 세 번째 주요 포인트

## 기술적 세부사항
구체적인 기술적 내용과 설명

## 영향 및 전망
이 뉴스가 개발자 커뮤니티나 기술 산업에 미칠 영향

## 참고 자료
관련 링크나 추가 정보

실제 최신 뉴스처럼 현실적이고 유용한 정보를 포함해주세요.
"""

    return get_gemini_response(prompt)

def create_jekyll_post(content, topic):
    """Jekyll 포스트 파일을 생성합니다."""
    
    # 현재 날짜
    today = datetime.now()
    date_str = today.strftime(DATE_FORMAT)
    time_str = today.strftime(TIME_FORMAT)
    
    # 파일명 생성 (한글 제목을 영문으로 변환)
    title_words = topic.replace(" ", "-").lower()
    filename = f"{date_str}-{title_words}-daily-news.md"
    
    # Jekyll front matter
    front_matter = f"""---
layout: {JEKYLL_LAYOUT}
title:  "{topic} - {date_str} Daily News"
date:   {date_str} {time_str}
categories: news {topic.lower().replace(" ", "-")}
tags: [news, {topic.lower().replace(" ", "-")}, daily]
---

"""
    
    # 전체 포스트 내용
    full_content = front_matter + content
    
    # _posts 디렉토리에 파일 저장
    posts_dir = Path(JEKYLL_POSTS_DIR)
    posts_dir.mkdir(exist_ok=True)
    
    file_path = posts_dir / filename
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"포스트 파일이 생성되었습니다: {file_path}")
        return str(file_path)
    except Exception as e:
        print(f"파일 저장 오류: {e}")
        return None

def main():
    """메인 함수"""
    print("=== Daily News Post Generator ===")
    
    # 랜덤하게 주제 선택
    selected_topic = random.choice(NEWS_TOPICS)
    print(f"선택된 주제: {selected_topic}")
    
    # 뉴스 내용 생성
    print("뉴스 내용을 생성 중...")
    news_content = generate_news_content(selected_topic)
    
    if not news_content:
        print("뉴스 내용 생성에 실패했습니다.")
        sys.exit(1)
    
    print("뉴스 내용 생성 완료!")
    
    # Jekyll 포스트 파일 생성
    print("Jekyll 포스트 파일을 생성 중...")
    file_path = create_jekyll_post(news_content, selected_topic)
    
    if file_path:
        print(f"✅ 성공적으로 포스트가 생성되었습니다: {file_path}")
        
        # 생성된 내용 미리보기
        print("\n=== 생성된 포스트 미리보기 ===")
        print(news_content[:500] + "..." if len(news_content) > 500 else news_content)
    else:
        print("❌ 포스트 생성에 실패했습니다.")
        sys.exit(1)

if __name__ == "__main__":
    main() 