# Spring Boot Todo API - 첫 번째 CRUD

> 2026-06-08

## 배운 것

### 1. 환경 세팅

- JDK 17 (LTS, Spring Boot 3.x 필수)
- IntelliJ IDEA Community
- Spring Initializr (start.spring.io) 로 프로젝트 생성
  - SNAPSHOT, RC 붙은 버전은 불안정 → 정식 릴리즈만 사용
  - Dependencies: Spring Web, Spring Data JPA, MySQL Driver, Lombok

### 2. 프로젝트 구조

```
todoapi
├── entity/
│   └── Todo.java           # DB 테이블 매핑
├── repository/
│   └── TodoRepository.java # DB 접근
├── service/
│   └── TodoService.java    # 비즈니스 로직
├── controller/
│   └── TodoController.java # HTTP 요청/응답
└── dto/
    └── TodoCreateRequest.java # 클라이언트 요청 데이터
```

### 3. 레이어 구조와 역할

```
클라이언트 (Postman / 브라우저)
    ↓ HTTP 요청
Controller   → 요청 받고 응답 돌려줌. 로직 없음
    ↓
Service      → 실제 비즈니스 로직 처리
    ↓
Repository   → DB 저장/조회/삭제
    ↓
DB (H2 / MySQL)
```

각 레이어는 자기 역할만 알고, 나머지는 몰라도 됨. 이게 레이어 분리의 핵심.

### 4. 어노테이션 정리

| 어노테이션 | 역할 |
|-----------|------|
| `@Entity` | 이 클래스가 DB 테이블임을 JPA에게 알림 |
| `@Id` | 기본키 지정 |
| `@GeneratedValue` | id 자동 증가 (1, 2, 3...) |
| `@Getter` | Lombok - getter 메서드 자동 생성 |
| `@NoArgsConstructor` | Lombok - 빈 생성자 자동 생성 (JPA 필수) |
| `@AllArgsConstructor` | Lombok - 전체 필드 생성자 자동 생성 (Builder 필수) |
| `@Builder` | Lombok - Builder 패턴 자동 생성 |
| `@Service` | 스프링이 이 클래스를 서비스 빈으로 관리 |
| `@RequiredArgsConstructor` | Lombok - final 필드를 생성자로 자동 주입 |
| `@RestController` | 컨트롤러 + JSON 응답 자동 처리 |
| `@RequestMapping` | 기본 URL 경로 지정 |
| `@GetMapping` | GET 요청 처리 |
| `@PostMapping` | POST 요청 처리 |
| `@RequestBody` | JSON → Java 객체 변환 |

### 5. Entity

```java
@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Todo {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long userId;
    private String content;
    private LocalDateTime createdAt;
    private Boolean finished;
}
```

- JPA가 카멜케이스를 자동으로 스네이크케이스로 변환
  - `createdAt` → `created_at`
  - `userId` → `user_id`

### 6. Repository

```java
public interface TodoRepository extends JpaRepository<Todo, Long> {
}
```

- `JpaRepository<Todo, Long>` 상속만 해도 기본 메서드 공짜로 생김
  - `save()` → INSERT / UPDATE
  - `findAll()` → SELECT *
  - `findById()` → SELECT WHERE id=?
  - `deleteById()` → DELETE WHERE id=?

### 7. DTO를 쓰는 이유

Entity를 직접 클라이언트에게 받으면 안 됨:
- `id`, `createdAt`, `finished` 같은 서버가 제어해야 할 값을 클라이언트가 조작 가능
- 보안 문제 → DTO로 받을 필드만 명시적으로 제한

```java
// 클라이언트한테 받을 것만
public class TodoCreateRequest {
    private Long userId;
    private String content;
}
```

### 8. Builder 패턴

```java
// 생성자 방식 (순서 틀리면 버그)
Todo todo = new Todo(1L, "공부하기", LocalDateTime.now(), false);

// Builder 방식 (필드 이름 보여서 명확)
Todo todo = Todo.builder()
        .userId(1L)
        .content("공부하기")
        .createdAt(LocalDateTime.now())
        .finished(false)
        .build();
```

### 9. 의존성 주입 (DI)

```java
// 직접 생성 (나쁜 방식)
private TodoRepository todoRepository = new TodoRepository();

// 의존성 주입 (좋은 방식)
@RequiredArgsConstructor
public class TodoService {
    private final TodoRepository todoRepository; // 스프링이 알아서 넣어줌
}
```

- `final` → 한 번 정해지면 못 바꿈, 안정적
- 스프링이 객체를 만들어서 넣어줌 → 테스트할 때 가짜로 바꿔치기 가능

### 10. 완성된 API

| 메서드 | URL | 설명 |
|--------|-----|------|
| GET | /todos | 전체 조회 |
| POST | /todos | Todo 생성 |

POST 요청 예시:
```json
{
    "userId": 1,
    "content": "오늘 공부하기"
}
```

응답 예시:
```json
{
    "id": 1,
    "userId": 1,
    "content": "오늘 공부하기",
    "createdAt": "2026-06-08T16:31:19.932907",
    "finished": false
}
```

## 막혔던 것 / 해결

- **H2 드라이버 에러** → `build.gradle`에 `runtimeOnly 'com.h2database:h2'` 추가
- **`createdAt` → `CREATE_AT`** → 오타였음. `createdAt` 으로 수정하니 `CREATED_AT` 으로 정상 변환
- **`@Builder` + `@NoArgsConstructor` 충돌** → `@AllArgsConstructor` 같이 추가해야 함

## 참고

- [Spring Initializr](https://start.spring.io)
- [Adoptium JDK 17](https://adoptium.net/)
- Spring Boot 3.x → JDK 17 이상 필수
- SNAPSHOT, RC 버전 쓰지 말 것
