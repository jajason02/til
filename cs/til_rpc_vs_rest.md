# RESTful vs RPC

> 2026-06-23

## 배운 것

**REST (Representational State Transfer)**

리소스(명사) 중심 설계. URL은 자원을 가리키고, HTTP 메서드가 그 자원에 대한 행동을 표현한다.

```
GET    /books/42        → 책 42번 조회
POST   /books           → 책 생성
PUT    /books/42        → 책 42번 수정
DELETE /books/42        → 책 42번 삭제
```

- URL = 명사 (자원의 위치)
- HTTP 메서드 = 동사 (행위)
- Stateless: 서버가 클라이언트 상태를 저장하지 않음
- 외부에 공개되는 API, 범용 클라이언트(브라우저, 앱 등)와의 통신에 적합

**RPC (Remote Procedure Call)**

행위(동사) 중심 설계. URL 자체가 "어떤 함수를 실행할지"를 나타낸다. HTTP는 전송 수단일 뿐.

```
POST /analyze_reviews   → 리뷰 분석 함수 실행
POST /generate_ideas    → 아이디어 생성 함수 실행
POST /suggest_plot      → 플롯 제안 함수 실행
```

- URL = 동사 (실행할 행위)
- HTTP 메서드는 거의 POST만 사용
- 요청/응답 포맷을 사전에 합의하는 구조
- 내부 서버 간 통신, 특정 작업 실행이 목적인 경우에 적합

**비교**

| 항목 | REST | RPC |
|---|---|---|
| URL 설계 | 명사 (자원) | 동사 (행위) |
| HTTP 메서드 | GET/POST/PUT/DELETE 구분 | 주로 POST |
| 중심 개념 | 리소스 상태 표현 | 함수 원격 호출 |
| 적합한 상황 | 외부 공개 API, CRUD 중심 | 내부 통신, 연산 중심 |
| 예시 | Django REST Framework | FastAPI AI 서버, gRPC |

**AI 추론 서버에 RPC가 맞는 이유**

REST는 자원(리소스)의 상태를 다루는 구조인데, AI 추론은 자원을 조회/저장하는 게 목적이 아니라 연산(행위) 자체가 목적이다.

- "리뷰를 분석해줘" → 분석 결과는 서버에 저장되지 않음, 행위 실행이 목적
- "아이디어를 생성해줘" → 생성이라는 연산 자체가 핵심, CRUD 아님

억지로 REST로 설계하면 `/reviews/analysis` 같은 어색한 명사형 URL이 생기고, 표현하고 싶은 "분석 행위"가 URL에서 드러나지 않는다.

**실무 정리**

- Django (외부 API) → RESTful. 클라이언트(Vue)가 소비하는 공개 API이므로 리소스 중심이 맞다.
- FastAPI (내부 AI 서버) → RPC. Django에서만 호출하는 내부 서버이고, 목적이 연산 실행이므로 RPC가 자연스럽다.

두 스타일을 혼용하는 건 잘못이 아니다. 어디에, 왜 쓰는지에 따라 적합한 설계가 다르다.


## 막혔던 것 / 해결

<!-- 어디서 막혔고 어떻게 해결했는지 -->

## 참고

<!-- 링크, 문서 등 -->
