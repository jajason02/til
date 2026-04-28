# 비트마스킹으로 상태 추적하기

> 2026-04-28

## 배운 것

비트마스킹은 정수의 각 비트를 플래그처럼 사용해 여러 상태를 동시에 관리하는 기법.

특정 범위 내 원소의 포함 여부를 효율적으로 추적할 수 있음.

**핵심 연산:**
- `visited |= (1 << num)`: num번째 비트를 1로 설정 (상태 포함)
- `total = (1 << n) - 1`: n개 비트가 모두 1인 상태 (완벽한 상태 정의)
- `visited == total`: 모든 상태가 포함되었는지 검사

```python
# 0~9의 모든 숫자를 봤는가?
total = (1 << 10) - 1  # 0b1111111111

visited = 0
for digit in "2468":
    visited |= (1 << int(digit))
    
# visited = 0b0101010100
# visited == total  # False (모든 숫자를 못 봤음)
```

**한꺼번에 N비트 검사하기:**

```python
# 개별 검사 (O(N))
for n in range(N):
    if M & (1 << n) == 0:
        return "OFF"
return "ON"

# 한꺼번에 비교 (O(1))
lastNBit = (1 << N) - 1  # N개의 1: 0b111...1
if lastNBit == (M & lastNBit):
    return "ON"
else:
    return "OFF"
```

원리: `M & lastNBit`로 M의 하위 N비트만 추출해서, 완벽한 상태(`lastNBit`)와 비교.
M의 상위 비트는 AND에서 자동으로 0이 되므로 무시됨.

## 막혔던 것 / 해결

`visited |= (1 << num)` vs `visited = (1 << num)` 차이를 명확히 함.
- `|=` 연산자는 기존 비트를 유지하면서 누적
- `=` 연산자는 이전 정보를 모두 덮어씀

`visited & total == total` vs `visited == total` 비교:
- `==`: 초과 비트까지 정확히 검사 (권장)
- `&`: 필요한 비트만 확인, 초과 비트는 무시

실제 코드에서는 비트 관리가 정확하면 둘 다 작동하지만, 안전성 측면에서 `==` 사용이 나음.

## 참고

SWEA 문제에서 자주 등장하는 최적화 기법.
메모리와 속도 면에서 Set/List 대비 우수.
비트마스킹 + DP 조합으로 부분집합 문제 해결 가능.