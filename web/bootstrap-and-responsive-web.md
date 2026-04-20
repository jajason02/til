# Bootstrap & 반응형 웹

> 2026-02

## 배운 것

### Bootstrap

CSS 프론트엔드 프레임워크. 미리 정의된 클래스로 스타일/레이아웃을 빠르게 적용.

**Spacing 규칙**: `{property}{sides}-{size}`

```
mt-3  →  margin-top: 1rem (16px)
px-2  →  padding-left + padding-right: 0.5rem
```

| size | rem | px |
|:---|:---|:---|
| 0 | 0 | 0 |
| 1 | 0.25rem | 4px |
| 2 | 0.5rem | 8px |
| 3 | 1rem | 16px |
| 4 | 1.5rem | 24px |
| 5 | 3rem | 48px |

**Color System**: `primary`, `danger`, `success` 등 의미 기반 색상 사용.

**Component**: Alerts, Badges, Cards, Navbar, Modal 등 재사용 가능한 독립 UI 단위.

### 반응형 웹 — Grid System

12컬럼 기반. `row` 안에 `col-*`로 레이아웃 구성.

**Breakpoints**

| | xs | sm | md | lg | xl | xxl |
|:---|:---|:---|:---|:---|:---|:---|
| 기준 | <576px | ≥576px | ≥768px | ≥992px | ≥1200px | ≥1400px |

### Semantic Web

의미 있는 태그로 구조화 → 가독성, 접근성, SEO에 유리.

`<header>` `<nav>` `<main>` `<article>` `<section>` `<aside>` `<footer>`

**OOCSS**: 구조와 스킨 분리, 컨테이너와 콘텐츠 분리 → 재사용성 향상.

## 막혔던 것 / 해결

Grid에서 12컬럼을 초과하면 자동으로 다음 줄로 넘어가는 걸 몰랐음.  
`col-6` 두 개면 딱 맞고, `col-7 + col-6`이면 두 번째가 다음 줄로 내려감.
