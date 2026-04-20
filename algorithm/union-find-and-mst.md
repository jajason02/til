# Union-Find & 최소 신장 트리 (MST)

> 2026-04-16

## 배운 것

### Union-Find (서로소 집합)

두 원소가 같은 집합인지 확인하는 자료구조.

```python
p = [i for i in range(N + 1)]
rank = [0] * (N + 1)

def find_set(x):          # 대표 찾기 (경로 압축)
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):          # 두 집합 합치기 (랭크 기반)
    rx, ry = find_set(x), find_set(y)
    if rx == ry:
        return False
    if rank[rx] > rank[ry]:
        p[ry] = rx
    else:
        p[rx] = ry
        if rank[rx] == rank[ry]:
            rank[ry] += 1
    return True
```

### MST (최소 신장 트리)

N개 정점, N-1개 간선으로 모든 정점을 연결하는 트리 중 가중치 합이 최소인 것.

**Prim**: 방문한 정점 집합에서 가장 싼 간선을 greedy하게 선택. 우선순위 큐 사용. O(E log V).

**Kruskal**: 모든 간선을 가중치 오름차순 정렬 후 사이클 없으면 추가. Union-Find 사용. O(E log E).

| | Prim | Kruskal |
|:---|:---|:---|
| 적합한 경우 | 간선이 많은 밀집 그래프 | 간선이 적은 희소 그래프 |
| 핵심 자료구조 | 우선순위 큐 | Union-Find |

## 막혔던 것 / 해결

경로 압축 없이 `find_set`을 쓰면 트리가 길어져 O(n)으로 느려짐.  
`p[x] = find_set(p[x])`로 재귀하면서 경로를 평탄화하면 거의 O(1)에 수렴.
