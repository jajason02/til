# BFS (너비 우선 탐색)

> 2026-04-16

## 배운 것

시작 노드에서 가까운 노드부터 순서대로 탐색. 큐(Queue) + 방문 처리로 구현.

**핵심 원칙**
- 큐에 **넣을 때** 바로 visited 처리 (꺼낼 때 하면 중복이 큐에 쌓임)
- `deque.popleft()` 사용 — `list.pop(0)`은 O(n), `deque`는 O(1)

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)      # 넣을 때 방문 처리
                queue.append(neighbor)
```

**BFS가 최단 경로를 보장하는 이유**: 거리 1인 노드를 다 보고 나서 거리 2를 봄. 처음 도달한 순간이 곧 최소 이동 횟수.

> 가중치 있는 그래프의 최단 경로는 BFS가 아니라 다익스트라(Dijkstra).

## 막혔던 것 / 해결

visited 처리를 `popleft()` 이후에 하면 같은 노드가 큐에 여러 번 들어가는 문제 발생.  
큐에 `append()` 하는 시점에 바로 visited에 추가해야 함.
