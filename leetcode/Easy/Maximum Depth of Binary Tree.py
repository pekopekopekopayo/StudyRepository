# 트리를 입력으로 받는다.
# 트리의 최대 깊이를 반환하라


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 전역 변수 하나 생성
        global answer
        answer = 0

        # 깊이는 깊이로 잡아야지 dfs 깊이 탐색
        def dfs(node, cnt):
            global answer
            # 왼쪽 오른쪽 둘다 탐색을 한다.
            # 더 이상 노드가 없다면 깊이의 최대 값을 구한다.
            if node:
                dfs(node.left, cnt+1)
                dfs(node.right, cnt+1)
            else: 
                answer = max(answer, cnt)
        dfs(root, 0)
        return answer