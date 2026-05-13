# DOM

> 2026-05-13

## 배운 것

### DOM이란?
* 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
* 문서 구조, 스타일, 내용 등을 변경할 수 있게 함

### document 객체
* 웹을 나타내는 DOM 트리의 최상위 객체
* document 의 하위 객체로 <html>, <head>, <body> 등이 들어감
```javascript
// DOM 선택
document.querySelector(selector) // 선택자 한개 선택 (ex: '.content', '#id', 'p', 'h1')
document.querySelectorAll(selector) // 선택자와 일치하는 여러 요소 선택

// DOM 조작
// 클래스 속성 조작 메서드
element.classList.add() // 지정한 클래스 값을 추가
element.classList.remove() // 지정한 클래스 값을 제거
element.classList.toggle() // 클래스가 존재한다면 제거하고 false, 존재하지 않으면 추가 후 true 반환

// 일반 속성 조작 메서드
Element.getAttribute() // 해당 요소에 지정된 값을 반환
Element.setAttribute(name, value) // 지정된 요소의 속성 값을 설정 (예: 'href', 'https://www.naver.com')
Element.removeAttribute() // 요소에서 지정된 이름을 가진 속성 제거

//DOM 요소 제작 메서드
document.createElement(tagName) // 작성한 tagName의 HTML 요소를 생성, 반환
Node.appendChild() // 한 노드를 특정 부모 노드의 자식 리스트 중 마지막으로 삽입, 반환
Node.removeChild() // DOM에서 자식 노드를 제거, 반환

```

## 막혔던 것 / 해결

document도 하나의 객체라는 것을 처음 잘 몰라서 이해를 못했다.
알고 나니 메서드에 document를 넣는 이유를 알 것 같다.

## 참고

