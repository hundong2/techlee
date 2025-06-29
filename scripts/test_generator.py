#!/usr/bin/env python3
"""
Daily News Generator Test Script
뉴스 생성기를 테스트하는 스크립트
"""

import os
import sys
from pathlib import Path

# 현재 디렉토리를 scripts로 변경
script_dir = Path(__file__).parent
os.chdir(script_dir)

# 메인 스크립트 import
from generate_news_post import main

def test_generator():
    """뉴스 생성기를 테스트합니다."""
    print("🧪 Daily News Generator 테스트 시작")
    
    # 환경 변수 확인
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.")
        print("다음 명령어로 API 키를 설정하세요:")
        print("export GEMINI_API_KEY='your-api-key-here'")
        return False
    
    print("✅ API 키가 설정되어 있습니다.")
    
    # 메인 함수 실행
    try:
        main()
        print("✅ 테스트가 성공적으로 완료되었습니다!")
        return True
    except Exception as e:
        print(f"❌ 테스트 중 오류가 발생했습니다: {e}")
        return False

if __name__ == "__main__":
    success = test_generator()
    sys.exit(0 if success else 1) 