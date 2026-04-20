# 병합 정렬 (Merge Sort)

> 2026-04-16

## 배운 것

분할 정복(Divide & Conquer) 기반 정렬. 시간복잡도 O(n log n) 보장 (최악도 동일).

**과정**
1. 배열을 절반씩 재귀적으로 나눔 (원소 1개가 될 때까지)
2. 나눈 배열을 크기 비교하며 합침 (merge)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l]); l += 1
        else:
            result.append(right[r]); r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result
```

## 막혔던 것 / 해결

인덱스 기반 구현에서 `left_e`, `right_s`가 겹치는 구간 처리가 헷갈렸음.  
슬라이싱 버전으로 먼저 이해하고 나서 인덱스 버전을 보니 훨씬 명확해졌음.
