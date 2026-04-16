# 힙 (Heap)

> 2025-04-16

## 배운 것

완전 이진 트리 기반 자료구조. 최댓값/최솟값을 O(1)에 조회.

- **최대힙**: 부모 키 > 자식 키. 루트 = 최댓값.
- **최소힙**: 부모 키 < 자식 키. 루트 = 최솟값.
- 완전 이진 트리라 배열로 표현 가능. 부모 인덱스 = 자식 인덱스 // 2

**삽입**: 맨 뒤에 넣고 부모와 비교하며 위로 올라감 (sift-up).  
**삭제**: 루트를 꺼내고 마지막 노드를 루트로 올린 뒤 아래로 내려보냄 (sift-down).

**Python `heapq` 사용 (기본 최소힙)**

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heapq.heappop(heap))  # 1

# 최대힙으로 쓰려면 부호 반전
heapq.heappush(heap, -value)
result = -heapq.heappop(heap)
```

## 막혔던 것 / 해결

최대힙을 직접 구현할 때 sift-down에서 자식이 둘일 경우 더 큰 자식과 비교해야 하는 걸 빠뜨렸음.  
`heapq`는 최소힙만 지원하므로 최대힙이 필요하면 값에 `-`를 붙여야 함.
