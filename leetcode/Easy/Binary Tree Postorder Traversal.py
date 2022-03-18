# 2진 트리가 입력으로 주어진다.
# 후위 순회 한 값을 배열로 반환하여라.
# 후위 순회는 왼쪽 오른쪽 루트 기준이다.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from ast import List
from typing import Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        # 깊이 탐색이였기 때문에 dfs 사용
        def dfs(node):
          # 후위 순회는 왼쪽 오른쪽 루트 이다.
            if node:
                dfs(node.left)
                dfs(node.right)
                stack.append(node.val)
        dfs(root)
        return stack
        