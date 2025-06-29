# Daily News Generator

매일 정해진 시간에 Gemini API를 사용하여 기술 뉴스를 자동으로 생성하고 Jekyll 블로그 포스트로 만드는 시스템입니다.

## 🚀 기능

- **자동 뉴스 생성**: Gemini API를 사용하여 다양한 기술 주제의 뉴스 생성
- **Jekyll 포스트 자동 생성**: 생성된 뉴스를 Jekyll 블로그 포스트 형식으로 변환
- **GitHub Actions 자동화**: 매일 정해진 시간에 자동 실행
- **다양한 주제**: 15가지 기술 관련 주제에서 랜덤 선택

## 📋 필요 조건

1. **Gemini API 키**: Google AI Studio에서 API 키 발급
2. **GitHub 저장소**: Jekyll 블로그가 호스팅된 GitHub 저장소
3. **GitHub Actions 권한**: 저장소에 대한 쓰기 권한

## ⚙️ 설정 방법

### 1. Gemini API 키 설정

1. [Google AI Studio](https://makersuite.google.com/app/apikey)에서 API 키를 발급받습니다.
2. GitHub 저장소의 Settings > Secrets and variables > Actions로 이동합니다.
3. "New repository secret"을 클릭하고 다음을 입력합니다:
   - Name: `GEMINI_API_KEY`
   - Value: 발급받은 API 키

### 2. 실행 시간 설정

`.github/workflows/daily-news-generator.yml` 파일에서 실행 시간을 조정할 수 있습니다:

```yaml
schedule:
  # 매일 오전 9시 (한국 시간)에 실행
  - cron: '0 0 * * *'
```

### 3. 뉴스 주제 커스터마이징

`scripts/config.py` 파일에서 뉴스 주제를 추가하거나 수정할 수 있습니다:

```python
NEWS_TOPICS = [
    "기술 뉴스",
    "AI/머신러닝",
    # 원하는 주제 추가
]
```

## 🔧 수동 실행

GitHub Actions 탭에서 "Daily News Generator" 워크플로우를 선택하고 "Run workflow" 버튼을 클릭하여 수동으로 실행할 수 있습니다.

## 📁 파일 구조

```
scripts/
├── generate_news_post.py    # 메인 뉴스 생성 스크립트
├── config.py               # 설정 파일
└── README.md              # 이 파일

.github/workflows/
└── daily-news-generator.yml # GitHub Actions 워크플로우

requirements.txt            # Python 의존성
```

## 📝 생성되는 포스트 형식

생성되는 Jekyll 포스트는 다음과 같은 형식을 가집니다:

```markdown
---
layout: post
title:  "기술 뉴스 - 2024-01-15 Daily News"
date:   2024-01-15 09:00:00 +0900
categories: news 기술-뉴스
tags: [news, 기술-뉴스, daily]
---

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
```

## 🛠️ 문제 해결

### API 키 오류
- GitHub Secrets에 API 키가 올바르게 설정되었는지 확인
- API 키가 유효한지 확인

### 파일 생성 실패
- `_posts` 디렉토리가 존재하는지 확인
- GitHub Actions에 쓰기 권한이 있는지 확인

### 뉴스 내용 생성 실패
- 인터넷 연결 상태 확인
- Gemini API 서비스 상태 확인

## 📞 지원

문제가 발생하거나 개선 사항이 있으면 GitHub Issues를 통해 문의해주세요.

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 