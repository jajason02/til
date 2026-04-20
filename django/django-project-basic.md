# 장고 프로젝트, 앱의 기본 구조, 실행 흐름

> 2026-04-20

## 배운 것

### 1. 프로젝트 urls.py에서 앱 URL 등록

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # include('myapp.urls') = myapp폴더 내 urls.py 파일을 가져온다.
    path('', include('myapp.urls')), 
]
```

### 2. 앱 urls.py에서 경로와 함수 연결

```python
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # path('경로', 실행할 함수, 이름)
    path('',views.index, name = 'index'),
    # about/ = 사용자가 입력할 URL 경로
    # views.about = 이 경로로 들어오면 실행할 python 함수
    # name='about' = 템플릿에서 'myapp:about' 으로 참조 가능
    path('about/', views.about, name='about'),
    path('article/<int:id>/', views.article, name='article'),
]
```
### 3. view.py 에서 함수 정의
``` python
# myapp/views.py
from django.shortcuts import render
from .models import Article

# 가장 기본적인 함수
def index(request):
    """
    request: 사용자 요청 정보를 담은 객체
    - GET 파라미터, POST 데이터, 사용자 정보 등 모두 여기 있음
    """
    # 1. 데이터 준비 (DB에서 가져오거나, 계산하거나)
    articles = Article.objects.all()  # DB에서 모든 글 가져오기
    
    # 2. 템플릿 렌더링 (HTML + 데이터 조합)
    return render(
        request,
        'myapp/index.html',  # ← 어느 HTML 파일 사용할지
        {'articles': articles}  # ← HTML에 전달할 데이터 (딕셔너리)
    )


def about(request):
    """더 간단한 예: 데이터 없이 그냥 HTML만 반환"""
    return render(request, 'myapp/about.html')


def article(request, id):
    """
    URL에서 받은 변수
    - urls.py에서 <int:id> 로 정의했으니 id가 정수로 들어옴
    """
    article = Article.objects.get(id=id)  # DB에서 특정 글 1개 가져오기
    
    return render(
        request,
        'myapp/article.html',
        {'article': article}  # 템플릿에서 {{ article.title }} 이렇게 사용 가능
    )
```

### 4. HTML 템플릿에서 데이터 표현
```html
<!-- myapp/templates/myapp/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>글 목록</title>
</head>
<body>
    <h1>모든 글</h1>
    
    <!-- views.py에서 {'articles': articles} 로 보낸 데이터 사용 -->
    {% for article in articles %}
        <div>
            <h2>{{ article.title }}</h2>
            <p>{{ article.content }}</p>
            <!-- URL 역참조: name으로 정의한 경로 자동으로 생성 -->
            <a href="{% url 'myapp:article' article.id %}">
                자세히 보기
            </a>
        </div>
    {% endfor %}
</body>
</html>
```

### 전체 흐름
```
사용자가 브라우저에서 "localhost:8000/about/" 입력
        ↓
프로젝트의 urls.py에서 패턴 찾음
        ↓
"" include('myapp.urls') 하니까 myapp/urls.py 확인
        ↓
myapp/urls.py에서 'about/' 찾음!
        ↓
views.about 함수 실행
        ↓
render(request, 'myapp/about.html') 실행
        ↓
myapp/templates/myapp/about.html 파일 찾음
        ↓
HTML 렌더링해서 사용자 브라우저에 전송
        ↓
브라우저가 HTML 표시
```

## 막혔던 것 / 해결
<!-- 어디서 막혔고 어떻게 해결했는지 -->
1. 일단 urls 파일이 두개나 있고, 뭐는 함수고 뭐는 클래스고 import도 많아서 뭐가 어떤 역할을 하는지가 직관적으로 이해가 되지 않았다. 그래서 생성형 AI의 도움을 통해 사용자의 응답에 따라 프로그램이 움직이는 흐름을 정리해서 이해할 수 있었다.
## 참고

<!-- 링크, 문서 등 -->
