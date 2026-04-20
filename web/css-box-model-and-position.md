# CSS Box Model & Position

> 2026-02

## 배운 것

### 박스 타입

| 타입 | 줄바꿈 | width/height | 상하 margin |
|:---|:---|:---|:---|
| `block` | O (한 줄 전체 차지) | 사용 가능 | 적용됨 |
| `inline` | X (콘텐츠 크기만) | 사용 불가 | 적용 안됨 |
| `inline-block` | X | 사용 가능 | 적용됨 |
| `none` | - | 공간 자체 사라짐 | - |

### Position 유형

| 값 | 기준 | Normal Flow |
|:---|:---|:---|
| `static` | 기본값 | 유지 |
| `relative` | 자기 원래 위치 | 유지 (공간 차지) |
| `absolute` | 가장 가까운 relative 부모 | 제거 (공간 사라짐) |
| `fixed` | 뷰포트 | 제거 |
| `sticky` | 스크롤 임계점 전: relative, 후: fixed | 유지 |

### z-index

- 값이 클수록 위에 쌓임. `static`에는 적용 안됨.
- 부모의 z-index가 낮으면 자식이 아무리 높아도 부모 위로 못 올라감.

## 막혔던 것 / 해결

`absolute`가 뷰포트 기준으로 움직여서 당황했는데, 부모에 `position: relative`가 없어서였음.  
`absolute`는 반드시 `relative` 부모가 필요하다는 걸 기억.
