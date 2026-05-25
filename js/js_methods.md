# JS 메서드 정리

> 2026-05-18

## 배운 것

### 배열 메서드
* `filter()`: 조건에 맞는 요소만 새 배열로 반환
* `map()`: 각 요소를 변환하여 새 배열로 반환
* `find()`: 조건에 맞는 첫 번째 요소 반환 (배열 아님)
* `forEach()`: 각 요소를 순회, 반환값 없음
* `reduce()`: 누적값 계산하여 단일 값 반환
* `join()`: 배열 요소를 구분자로 합쳐 문자열 반환
* `push()`: 배열 맨 뒤에 요소 추가
* `unshift()`: 배열 맨 앞에 요소 추가
* `shift()`: 배열 첫 번째 요소 제거 및 반환
* `includes()`: 특정 값 포함 여부 boolean 반환
* `slice()`: 배열/문자열 일부 잘라서 반환 (원본 유지)

### 객체 관련
* 단축 구문: 키와 변수명이 같으면 `{ name: name }` → `{ name }`
* 계산된 속성명: `{ [expression]: value }` 대괄호로 동적 키 생성
* 단축 메서드: `{ greet: function() {} }` → `{ greet() {} }`

### 함수
* 기본 인자값: `function(n, m = 2)` — 인자 없으면 기본값 사용
* 화살표 함수에서 `this`: 상위 스코프 `this` 상속 → 메서드 콜백에 유용
* 일반 함수에서 `this`: 호출 방식에 따라 달라짐 → 객체 메서드는 일반 함수 사용

```javascript
// filter
const result = arr.filter((el) => el !== null);

// map
const speeds = trips.map((trip) => trip.distance / trip.time);

// find vs filter
accounts.find((a) => a.balance === 24000);    // 객체 반환
accounts.filter((a) => a.balance === 24000);  // 배열 반환

// reduce
arr.reduce((acc, cur) => acc + cur, 0);

// 계산된 속성명
const city = 'Seoul';
const obj = { [`livesIn${city}`]: true };  // { livesInSeoul: true }
```

## 막혔던 것 / 해결

* `forEach` 콜백에서 `this` 안 잡힘 → 화살표 함수로 변경해서 해결
* `shift(str)`에 인자 넣어봤는데 무시됨 → `shift()`는 인자 없이 첫 요소 제거, 앞에 추가는 `unshift()` 사용

## 참고
