# 이진 탐색 트리 (BST)

> 2026-04-16

## 배운 것

**조건**: 왼쪽 서브트리 키 < 루트 키 < 오른쪽 서브트리 키. 모든 키는 유일.

- 평균 탐색/삽입/삭제: O(log n)
- 최악(한쪽으로 치우친 경우): O(n)
- 중위 순회 시 오름차순 정렬된 결과

```python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def search(root, key):
    if key == root.key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
```

## 막혔던 것 / 해결

BST가 정렬된 상태로 삽입되면 한쪽으로 쏠려서 성능이 O(n)으로 떨어짐.  
이를 해결하는 게 AVL 트리, 레드-블랙 트리 같은 균형 BST.
