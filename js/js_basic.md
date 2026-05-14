# 자바 기본 문법

> 2026-05-14

## 배운 것

### 참조 자료형
* array: 파이썬의 리스트, Object: 파이썬의 딕셔너리임
* null: 개발자가 정의한 빈 값,  undefined: 시스템 상 값이 할당되지 않았음
* 동등 연산자(==), 일치 연산자(===) 다름
  * 동등 연산자는 암묵적 타입 변환, 객체일 경우 메모리 주소를 판별 -> 앵간하면 === 쓰자


```javascript
for ([key, value] of Object.entries(obj)) // 오브젝트는 non-iterable이어서 for ... of 안됨. entries로 iterable로 바꿔줌
if (Array.isArray(value)) // value 변수가 리스트인지 확인


```

## 막혔던 것 / 해결

map은 iterable이어서 for ... of가 가능했는데 Obj는 안되어서 당황했다. 메서드를 알아낸 후 쉽게 처리할 수 있었다

## 참고
