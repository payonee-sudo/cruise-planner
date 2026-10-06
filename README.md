# 항해표 — 가족 크루즈 플래너

직장인 가족이 취향, 지역, 출발 월, 여행 기간과 선사를 조합해 크루즈 여행을 탐색하는 반응형 웹사이트입니다.

## 주요 기능

- 10가지 사진형 여행 취향 선택
- 취향별 4개 지역 추천과 시네마틱 무음 루프
- 2026년 4분기부터 2030년까지 월별 탐색
- 기간·선사·인원·객실 등급에 따른 일정 및 예상 예산
- 기항지 추천과 예약처 비교 안내
- 주요 선사 5곳의 감성적인 특징 소개
- 모바일 반응형 UI와 `prefers-reduced-motion` 지원

## 실행

빌드 과정 없이 `dist/index.html`을 열거나 정적 웹 서버로 `dist` 폴더를 제공하면 됩니다.

```bash
python3 -m http.server 4173 --directory dist
```

## 배포 사이트

[항해표 라이브 사이트](https://hanghaepyo-family-cruise.wavy-fawn-5688.chatgpt.site/)

## 폴더 구조

- `dist/`: 배포 가능한 정적 사이트
- `assets/generated/`: 생성 이미지 원본 시트
- `scripts/`: 정적·모션 자산 생성 스크립트
- `references/`: 크루즈 일정·예산 구성 규칙
- `agents/`, `SKILL.md`: 재사용 가능한 Codex 스킬 정의

