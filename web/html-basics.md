# HTML 기초

> 2026-02

## 배운 것

HyperText Markup Language. 태그로 문서 구조를 명시하는 마크업 언어.

**요소(Element)**: 여는 태그 + 내용 + 닫는 태그로 구성. 닫는 태그 없는 태그도 존재(`<img>`, `<meta>` 등).

**속성(Attribute)**: 태그에 추가 정보 부여. 요소 이름과 공백으로 구분, 값은 따옴표로 감쌈.

```html
<p class="editor-note">My cat is very grumpy</p>
```

**기본 문서 구조**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <h1>제목</h1>
  <p>단락 <strong>굵게</strong> <em>기울임</em></p>
  <a href="https://www.google.com">링크</a>
  <img src="image.png" alt="설명">
  <ol><li>순서 있는 목록</li></ol>
  <ul><li>순서 없는 목록</li></ul>
</body>
</html>
```

**자주 쓰는 태그 요약**

| 태그 | 용도 |
|:---|:---|
| `<h1>~<h6>` | 제목 |
| `<p>` | 문단 |
| `<a href="">` | 하이퍼링크 |
| `<img src="" alt="">` | 이미지 |
| `<strong>` | 굵게 (의미 강조) |
| `<em>` | 기울임 (의미 강조) |
| `<ol>` / `<ul>` | 순서 있는 / 없는 목록 |
