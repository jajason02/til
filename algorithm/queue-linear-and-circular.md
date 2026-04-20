# Queue — 선형 큐 & 원형 큐

> 2026-04-16

## 배운 것

### 선형 큐

FIFO 자료구조. `front`, `rear` 포인터로 관리.

```python
N = 10
q = [0] * N
front = rear = -1

# 삽입 (enqueue)
rear += 1
q[rear] = value

# 삭제 (dequeue)
front += 1
print(q[front])
```

**단점**: `dequeue` 해도 앞 공간이 재사용되지 않아 공간 낭비 발생.

### 원형 큐

선형 큐의 공간 낭비를 해결. 처음과 끝을 연결한 구조.

- `%` 연산자로 인덱스 순환: `rear = (rear + 1) % N`
- `front` 자리는 항상 비워둠 → 공백(`front == rear`)과 포화(`(rear+1) % N == front`) 구분

## 막혔던 것 / 해결

선형 큐에서 `front == rear`이면 빈 큐처럼 보이지만 실제론 포화일 수 있어서 헷갈렸음.  
원형 큐에서 `front` 자리를 비워두는 이유가 이 두 상태를 구분하기 위해서임.
