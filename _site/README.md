# techlee.github.io
Software Tech Blog with AI-Powered Daily News

## 🚀 자동 뉴스 생성 시스템

이 블로그는 Gemini API를 사용하여 매일 자동으로 기술 뉴스를 생성하는 시스템을 포함하고 있습니다.

### 📋 주요 기능
- **AI 기반 뉴스 생성**: Gemini API를 사용한 자동 뉴스 작성
- **GitHub Actions 자동화**: 매일 정해진 시간에 자동 실행
- **다양한 기술 주제**: 15가지 기술 관련 주제에서 랜덤 선택
- **Jekyll 블로그 통합**: 생성된 뉴스를 자동으로 블로그 포스트로 변환

### ⚙️ 설정 방법

1. **Gemini API 키 설정**
   - [Google AI Studio](https://makersuite.google.com/app/apikey)에서 API 키 발급
   - GitHub 저장소 Settings > Secrets > Actions에서 `GEMINI_API_KEY` 설정

2. **실행 시간 조정**
   - `.github/workflows/daily-news-generator.yml`에서 cron 설정 수정

3. **뉴스 주제 커스터마이징**
   - `scripts/config.py`에서 뉴스 주제 추가/수정

### 🔧 수동 실행
GitHub Actions 탭에서 "Daily News Generator" 워크플로우를 선택하고 "Run workflow" 버튼을 클릭하여 수동으로 실행할 수 있습니다.

### 📁 파일 구조
```
├── scripts/
│   ├── generate_news_post.py    # 메인 뉴스 생성 스크립트
│   ├── config.py               # 설정 파일
│   ├── test_generator.py       # 테스트 스크립트
│   └── README.md              # 상세 사용법
├── .github/workflows/
│   └── daily-news-generator.yml # GitHub Actions 워크플로우
├── requirements.txt            # Python 의존성
└── _posts/                    # 생성된 뉴스 포스트
```

자세한 사용법은 [scripts/README.md](scripts/README.md)를 참조하세요.

## 📦 Bundle GitHub Pages Update

```sh
bundle update github-pages
gem update github-pages
```

## 📞 지원

문제가 발생하거나 개선 사항이 있으면 GitHub Issues를 통해 문의해주세요.
