# CSS 기초

> 2026-02

## 배운 것

Cascading Style Sheet. HTML 요소에 스타일을 입히는 언어.

**적용 방법** (우선순위 낮은 순)
1. 외부 스타일 — 별도 `.css` 파일, `<link>`로 불러옴 (권장)
2. 내부 스타일 — `<head>` 안 `<style>` 태그
3. 인라인 스타일 — 태그의 `style` 속성 (비권장)

**선택자 종류**

```css
* { }             /* 전체 */
h1 { }            /* 요소 */
.class-name { }   /* 클래스 */
#id-name { }      /* 아이디 */
.parent > span { } /* 자식 결합자 */
.parent li { }    /* 자손 결합자 */
[class^="y"] { }  /* 속성 선택자 */
```

**명시도(우선순위)**: `!important` > 인라인 > id > class > 요소 > 소스 순서

**상속**
- 상속 O: `font`, `color`, `text-align`, `opacity` 등 텍스트 관련
- 상속 X: `width`, `height`, `border`, `margin`, `padding` 등 박스 모델

**CSS Box Model**: 모든 요소는 사각형 박스. Content → Padding → Border → Margin 순으로 구성.

## 막혔던 것 / 해결

명시도 계산이 헷갈렸는데, id > class > 요소 순서로 외우고 나서 정리됨.  
같은 명시도면 나중에 선언된 스타일이 적용됨.
