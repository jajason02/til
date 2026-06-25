# Git Flow & 형상관리

> 2026-06-26

## 배운 것

**Git Flow란**

브랜치를 역할별로 나눠 협업 충돌을 줄이는 브랜치 전략.

```
main        → 배포용. 직접 커밋 금지
develop     → 통합 브랜치. 기능 완료 시 여기로 merge
feature/*   → 기능 단위 작업 브랜치. develop에서 분기, 완료 후 develop으로 merge
```

**브랜치 운용 흐름**

```
develop → feature/ai-server 분기
         feature/accounts 분기
         feature/books 분기

각자 작업 완료 → develop으로 PR/merge → 통합 테스트 → main merge
```

- 기능별로 브랜치를 분리하면 서로 작업이 겹쳐 충돌이 나는 상황을 최소화할 수 있다
- 한 사람이 merge할 때 다른 사람 코드를 덮어쓰는 사고를 방지

**형상관리 (Configuration Management)**

소스코드·설정·DB 스키마 등 프로젝트 산출물의 변경 이력을 추적·관리하는 것.

Git이 형상관리 도구의 역할을 한다.

- 언제, 누가, 무엇을, 왜 바꿨는지 commit 단위로 추적 가능
- 문제 발생 시 특정 시점으로 rollback 가능
- 브랜치 전략은 형상관리를 팀 단위로 안전하게 운용하기 위한 규칙

**3인 협업에서 실제로 겪은 것**

Django 모델 테이블명 충돌이 대표적인 케이스.

- 각자 브랜치에서 작업 → develop merge 시점에 DB 스키마 불일치 발견
- Django가 `db_table` 없으면 `앱이름_모델명(소문자)`으로 자동 생성 → ERD 기준(BOOK)과 달라 충돌
- 해결: 모델 Meta에 `db_table` 명시해 스키마 기준 통일

```python
class Book(models.Model):
    class Meta:
        db_table = 'BOOK'
```

- 교훈: 브랜치 분리만으로는 부족하고, 공유 자원(DB 스키마, ERD)은 사전에 기준을 명확히 잡아야 한다

**커밋 컨벤션**

브랜치 전략과 함께 커밋 메시지 규칙도 형상관리의 일부다.

```
feat: 아이디어 생성 API 추가
fix: JWT 토큰 sessionStorage 전환
refactor: AI 서버 타임아웃 처리 분리
docs: ERD 테이블명 통일 내용 반영
```

- 메시지만 보고 변경 내용을 파악할 수 있어야 rollback이나 이슈 추적이 쉬워진다

## 막혔던 것 / 해결

## 참고

- [Atlassian Git Flow 가이드](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
