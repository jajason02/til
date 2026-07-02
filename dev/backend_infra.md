# 백엔드 인프라 개념 정리 (프록시 / 캐시 / GC / 스트림 / 압축 / CDN)

> 2026-07-03

## 배운 것

**L4 / L7 프록시(라우터)**
- L4: IP·포트만 보고 분산, 콘텐츠 무관. 동일 서버 여러 대에 부하 분산이 핵심 용도.
- L7: URL/헤더/쿠키 등 내용을 보고 라우팅. 기능별로 다른 서비스(Django/FastAPI)로 분기.
- 실무는 `L4(1차 분산) → L7(세밀한 라우팅) → 백엔드 서버들` 계층 구조. L4가 여러 L7 복제본 앞에서 부하 분산 + 장애 대응(SPOF 방지).
- 프록시 = 요청을 대신 전달하는 중개자(포워드=클라이언트 대신, 리버스=서버 대신). 라우팅 = 프록시가 내부적으로 쓰는 "어디로 보낼지" 판단 규칙.

**슬로우 쿼리 & DB 병목**
- 원인: 인덱스 부재/미사용, N+1(ORM), 락 경합, 커넥션 풀 고갈, 비효율적 조인, 대용량 데이터, 캐싱 부재, 읽기/쓰기 미분리.
- 진단 흐름: 슬로우 쿼리 로그 → `EXPLAIN` 실행계획 확인 → 원인 특정 → 대응(인덱스, `select_related`/`prefetch_related`, 캐싱, 파티셔닝, Read Replica).

**로컬 캐시 vs 리모트 캐시**
- 로컬 캐시: 애플리케이션과 같은 프로세스 메모리. 빠르지만 프로세스별 독립 → 서버 여러 대면 공유 안 됨.
- 리모트 캐시(Redis): 별도 프로세스(서버)에 저장, 네트워크로 통신. 여러 서버/워커가 하나의 캐시 공유 가능.

**프로세스 / 힙 / 스택 / GC**
- 힙·스택은 언어가 아니라 프로세스가 할당받은 메모리 공간의 영역(프로세스마다 독립적).
- Python GC: 참조 카운팅(기본) + 세대별 Mark-and-Sweep(순환 참조 보완).
- Java GC: 참조 카운팅 없이 도달 가능성 기반. Young(Eden/Survivor)·Old 세대 구조, Minor/Major(Full) GC. G1GC가 최신 기본값.

**Stream (두 종류 구분)**
- Collection Stream: 컬렉션을 함수형으로 가공(filter/map/collect), 지연 연산(lazy evaluation).
- I/O Stream: 파일/네트워크 데이터를 청크 단위로 처리. 파일 다운로드 시 메모리 절약의 핵심 (전체를 메모리에 안 올리고 버퍼 크기만큼만 흘려보냄).

```python
# 파일 다운로드 스트리밍 예시 (FastAPI)
def file_streamer(file_path: str):
    with open(file_path, "rb") as f:
        while chunk := f.read(1024 * 1024):
            yield chunk
```

- 항상 스트리밍이 정답은 아님: 작은 파일은 통째로 로드하는 게 구현 단순 + Content-Length 명시 가능 + 더 빠를 수 있음.

**gzip 압축**
- HTML/JSON/CSS/JS는 반복 패턴이 많아 압축 효율 높음(60~80% 감소). 이미지/동영상 등 이미 압축된 바이너리는 효과 없음.
- `Accept-Encoding` 요청 → `Content-Encoding: gzip` 응답. Nginx 또는 프레임워크 미들웨어에서 적용, 앱 서버보다 Nginx/CDN 레벨에서 처리하는 게 일반적.

**CDN**
- 전 세계 엣지 서버에 콘텐츠 캐싱 → 물리적 거리에 따른 지연시간 감소.
- 정적 콘텐츠(이미지, CSS, JS, 폰트)에 강함, 동적 데이터는 원본 서버까지 요청 필요.
- 요청 흐름: `사용자 → CDN → L4 → L7 → 백엔드 서버`. 원본 서버 부하 감소 + 트래픽 폭증 방어.

## 막혔던 것 / 해결

- FastAPI를 쓴 이유를 처음엔 "병렬 처리"로 생각했는데, 정확히는 **동기 블로킹 문제를 비동기 구조로 회피**한 것에 가까움. Django도 async 뷰가 되지만 ORM/AI 라이브러리가 완전 비동기가 아니고, 분리의 진짜 이점은 배포 독립성 + 의존성 분리 + 장애 격리라는 걸 정리하며 이해.
- Collection Stream(`.stream()`)과 I/O Stream(`InputStream`/`StreamingResponse`)을 같은 "스트림"으로 헷갈렸는데, 목적과 대상이 다른 별개 개념이라는 걸 구분.

## 참고

- Django `GZipMiddleware`, FastAPI `GZipMiddleware`
- Django `StreamingHttpResponse`, FastAPI `StreamingResponse`
