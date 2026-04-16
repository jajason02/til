# 백트래킹 & 순열 (Backtracking & Permutation)

> 2025-04-16

## 배운 것

**백트래킹**: 후보해를 쌓아가다 가능성이 없으면 되돌아가는 방식. 완전탐색을 가지치기로 효율화.

**핵심 흐름**
1. 선택
2. 유효성 검사 (가지치기)
3. 재귀로 다음 단계
4. **복구 (원상복원)** ← 제일 중요

```python
# N개 중 M개를 뽑는 순열
def backtrack(depth):
    if depth == M:
        print(*answer)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)

            backtrack(depth + 1)

            answer.pop()          # 복구
            visited[i] = False    # 복구
```

**자리 주인 방식 순열** (index 기반)

```python
def make_perm(idx, selected, result):
    if idx == N:
        print(result)
        return
    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            result.append(lst[i])
            make_perm(idx + 1, selected, result)
            selected[i] = 0
            result.pop()
```

## 막혔던 것 / 해결

재귀 호출 뒤에 `pop()`과 `visited = False` 복구를 빠뜨려서 결과가 이상하게 나왔음.  
백트래킹은 반드시 재귀 전후가 대칭 구조여야 함. 넣으면 반드시 빼야 함.
