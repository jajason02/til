# 트리 순회 (Tree Traversal)

> 2025-04-16

## 배운 것

트리의 노드를 체계적으로 방문하는 방법. 방문 순서에 따라 3가지.

| 순회 | 순서 | 활용 |
|:---|:---|:---|
| 전위 (Preorder) | 루트 → 왼쪽 → 오른쪽 | 트리 복사, 직렬화 |
| 중위 (Inorder) | 왼쪽 → 루트 → 오른쪽 | BST에서 오름차순 출력 |
| 후위 (Postorder) | 왼쪽 → 오른쪽 → 루트 | 트리 삭제, 수식 계산 |

```python
cleft = [0] * (N + 1)
cright = [0] * (N + 1)

def preorder(t):
    if t:
        print(t, end=" ")   # 루트 먼저
        preorder(cleft[t])
        preorder(cright[t])

def inorder(t):
    if t:
        inorder(cleft[t])
        print(t, end=" ")   # 가운데
        inorder(cright[t])

def postorder(t):
    if t:
        postorder(cleft[t])
        postorder(cright[t])
        print(t, end=" ")   # 루트 마지막
```

## 막혔던 것 / 해결

순회 이름이 루트의 방문 순서 기준임을 알고 나서 외우기 쉬워졌음.  
전위 = 루트가 **전**에, 중위 = 루트가 **중간**에, 후위 = 루트가 **후**에.
