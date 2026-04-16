# CSS Flexbox

> 2025-04-16

## 배운 것

요소를 행/열로 배치하는 1차원 레이아웃 방식. `display: flex`를 부모에 주면 자식들이 flex item이 됨.

**핵심 개념**
- **main axis**: item이 배치되는 기본 축 (기본값: 가로)
- **cross axis**: main axis에 수직인 축

**자주 쓰는 속성 정리**

```css
.container {
  display: flex;

  flex-direction: row | column | row-reverse | column-reverse;
  flex-wrap: nowrap | wrap;

  /* main axis 정렬 */
  justify-content: flex-start | center | flex-end | space-between | space-around;

  /* cross axis 정렬 (단일 행) */
  align-items: stretch | center | flex-start | flex-end;

  /* cross axis 정렬 (다중 행, wrap 필요) */
  align-content: stretch | center | flex-start | flex-end;
}

.item {
  /* 개별 아이템 cross axis 정렬 */
  align-self: auto | stretch | center | flex-start | flex-end;

  /* 남은 공간 비율로 차지 */
  flex-grow: 1;
}
```

## 막혔던 것 / 해결

`align-items`와 `align-content` 차이가 헷갈렸음.  
`align-items`는 한 줄 안에서 아이템 정렬, `align-content`는 여러 줄(wrap) 사이의 공간 분배.  
`flex-wrap: wrap`이 없으면 `align-content`는 의미 없음.
