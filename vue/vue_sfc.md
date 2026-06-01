# Vue SFC, 프로젝트 생성

> 2026-06-01

## 배운 것

### SFC (Single File Component)
Vue 컴포넌트를 `.vue` 파일 하나에 구조/로직/스타일(HTML, JS, CSS)를 모아 관리하는 방식.
구조를 담당하는 <template>, 로직을 담당하는 <script>, 스타일을 담당하는 <style> 세 부분

```vue
<template>
  <!-- HTML 구조 -->
  <div class="greeting">{{ message }}</div>
</template>

<script setup>
// JS 로직
import { ref } from 'vue'
const message = ref('Hello Vue!')
</script>

<style scoped>
/* CSS 스타일 */
.greeting {
    color: red;
}
</style>
```

---

### Vite와 npm의 역할

- **npm**: 패키지 설치/관리 도구. `node_modules` 관리. package.json 파일에 기록.
- **Vite**: 개발 서버 + 번들러. 코드 변경 시 즉시 반영(HMR).
- **build**: 프로젝트의 소스 코드를 최적화하고 번들링하여 배포할 수 있는 형식으로 변환하는 과정

```bash
npm create vue@latest   # Vue 프로젝트 생성
npm install             # 패키지 설치
npm run dev             # 개발 서버 실행
npm run build           # 배포용 빌드
```

---

### package.json vs package-lock.json

| | package.json | package-lock.json |
|---|---|---|
| 역할 | 프로젝트 설정, 의존성 목록 | 실제 설치된 버전 고정 |
| 버전 표기 | `^1.0.0` (범위) | `1.0.3` (정확한 버전) |
| 직접 수정 | O | X (자동 관리) |
| git 커밋 | O | O |

```json
// package.json
{
  "dependencies": {
    "vue": "^3.4.0"   // 3.x.x 범위 내 최신
  }
}

// package-lock.json
{
  "dependencies": {
    "vue": "3.4.21"   // 정확히 이 버전으로 고정
  }
}
```

---

### 자식 컴포넌트 등록

```vue
<!-- 부모: App.vue -->
<template>
  <Header/>
  <TodoList/>
</template>

<script setup>
import Header from './components/Header.vue'
import TodoList from './components/TodoList.vue'
</script>
```

`<script setup>`에서 Vue가 자동으로 import됨. 별도 등록 없이 바로 템플릿에서 사용 가능.

---

### style scoped

`scoped`를 붙이면 해당 컴포넌트에만 스타일 적용.

```vue
<style scoped>
/* ✅ 이 컴포넌트의 h1에만 적용 */
h1 { color: red; }
</style>

<style>
/* ❌ scoped 없으면 전역 적용 → 다른 컴포넌트에도 영향 */
h1 { color: red; }
</style>
```

---

### Virtual DOM

실제 DOM 조작은 비용이 큼 → Vue는 메모리에 가상 DOM을 만들어 비교 후 변경된 부분만 실제 DOM에 반영.
불필요한 렌더링을 줄여 성능을 크게 향상시킴.

```
상태 변경
  ↓
새로운 Virtual DOM 생성
  ↓
이전 Virtual DOM과 비교 (diffing)
  ↓
변경된 부분만 실제 DOM 업데이트 (patching)
```

```js
// 직접 DOM 조작 (느림)
document.querySelector('#title').textContent = 'Hello'

// Vue가 하는 일 (효율적)
// 1. title이 바뀌었다는 걸 감지
// 2. Virtual DOM 비교
// 3. textContent만 업데이트
```

주의사항
- 실제 DOM에 직접 접근 금지
    - querySelector, createElement 등
    - ref()와 Lifecycle Hooks 을 사용해 간접적으로 접근

### 용어 정리
스캐폴딩: 프로젝트를 만들 때 기본 뼈대 생성(startproject, vue@latest 등)
DOM: 문서 객체 모델
마운트: 컴포넌트를 DOM에 붙이는 것

## 막혔던 것 / 해결

- `<script src="...">` 랑 `<script setup>` 동시에 쓰면 충돌 → CDN 방식과 SFC 방식은 같이 못 씀
- `style scoped` 없이 쓰면 다른 컴포넌트 스타일까지 바뀌는 버그 → `scoped` 붙여서 해결

## 참고

- [Vue 공식 문서 - SFC](https://vuejs.org/guide/scaling-up/sfc.html)
- [Vite 공식 문서](https://vitejs.dev/)