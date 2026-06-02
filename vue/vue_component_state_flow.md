```markdown
# Props & Emit — 컴포넌트 간 데이터 흐름

> 2026-06-02

## 배운 것

### Props: 부모 → 자식 데이터 전달

부모가 v-bind로 데이터를 내려주고, 자식은 defineProps로 선언해서 받음

```vue
<!-- 부모 -->
<Child :message="msg" />

<!-- 자식 -->
<script setup>
// obj, array 모두 가능 가급적 obj 권장(유효성 검사를 통한 안정)
const props = defineProps({
  message: String
})
</script>
```

### Emit: 자식 → 부모 이벤트 전달

자식이 defineEmits로 이벤트 선언 후 emit으로 발신, 부모는 v-on(@)으로 수신
데이터도 같이 넘길 수 있음

```vue
<!-- 자식 -->
<script setup>
const emit = defineEmits(['some-event'])
emit('some-event', payload)
</script>

<!-- 부모 -->
<Child @some-event="handleEvent" />
```

## 막혔던 것 / 해결

- 파일명 대소문자(`secondComponent` vs `SecondComponent`) 충돌
- template(HTML) 에서는 kebab-case, script(js)에서는 camelCase 사용

## 참고

- [Vue 공식 문서 - Props](https://vuejs.org/guide/components/props.html)
- [Vue 공식 문서 - Events](https://vuejs.org/guide/components/events.html)
