# 두 트리가 입력으로 온다.
# 두 트리가 같은지 확인하고 True False를 반환 해라

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 깊이 탐색 트리는 다 깊이 탐색이 좋을 듯
        def dfs(q, p):
            # 두개가 다 있으면 실행
            if q and p:
                # 서로 값이 같으면 다음 검색 진행
                if q.val == p.val: return dfs(q.left,p.left) and dfs(q.right,p.right)
                # 만약 하나라도 틀리면 모든 값이 모두 False(꼬리 물기)
                else: return False
            # 하나는 있는데 하나는 없다? 그럼 같은 트리가 아님
            elif q or p:
                return False
            # 모든 조건을 충족 시키면 True를 반환
            return True
        # dfs실행 그리고 반환 값을 반환
        return dfs(q, p)
                
        