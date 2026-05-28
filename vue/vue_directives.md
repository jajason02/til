# Vue 디렉티브 정리

> 2026-05-27

## 배운 것

### v-bind — HTML 속성에 JS 값을 동적으로 바인딩
* 단축 문법: `v-bind:href="url"` → `:href="url"`
* 클래스/스타일은 객체나 배열도 받음: `:class="{ active: isActive }"`, `:style="{ color: textColor }"`
* 속성값이 문자열 그대로면 그냥 HTML, JS 변수/표현식이면 v-bind 사용

```html
<!-- 기본 -->
<a v-bind:href="url">링크</a>
<button v-bind:disabled="!isValid">제출</button>

<!-- 단축 -->
<a :href="url">링크</a>
<div :class="{ active: isActive, error: hasError }"></div>
<p :style="{ fontSize: size + 'px' }"></p>
```

### v-on — 이벤트 리스너 등록
* 단축 문법: `v-on:click="fn"` → `@click="fn"`
* 수식어(modifier) 체이닝 가능: `.prevent` `.stop` `.once` `.self`
* 키 수식어: `@keyup.enter`, `@keyup.esc`

```html
<!-- 기본 -->
<button v-on:click="handleClick">클릭</button>
<form v-on:submit.prevent="onSubmit"></form>

<!-- 단축 -->
<button @click="handleClick">클릭</button>
<button @click="count++">인라인 표현식도 OK</button>
<input @keyup.enter="search">
```

### v-model — 양방향 데이터 바인딩
* `v-bind + v-on` 합성: `:value="msg" + @input="msg = $event.target.value"`
* 수식어: `.lazy` (input → change 이벤트) / `.trim` (공백 제거) / `.number` (숫자 변환)

```html
<!-- input / textarea -->
<input v-model="message">
<textarea v-model="content"></textarea>

<!-- checkbox -->
<input type="checkbox" v-model="checked">

<!-- select -->
<select v-model="picked">
  <option value="a">A</option>
  <option value="b">B</option>
</select>

<!-- 수식어 -->
<input v-model.trim="username">
<input v-model.number="age">
<input v-model.lazy="query">
```

## 막혔던 것 / 헷갈렸던 것

* `v-bind`는 단방향(JS → DOM), `v-model`은 양방향 — 읽기 전용 표시에는 v-bind, 입력 폼에는 v-model
* `@click="fn"` vs `@click="fn()"` — 인자 없을 땐 괄호 생략 권장. 괄호 붙이면 `$event` 직접 넘겨야 이벤트 객체 받을 수 있음
* 컴포넌트에 `v-model` 쓰면 내부적으로 `modelValue` prop + `update:modelValue` emit으로 동작

## 참고
