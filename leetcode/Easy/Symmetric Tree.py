# 한 트리를 입력으로 받는다.
# 루트를 기준으로 왼쪽 자식 노드의 트리가 오른쪽 자식 노드의 트리와 상반(반대방향)여부를 True False 값을 반환하라

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 자식 노드가 없다면 True임 예외처리 안해서 혼났음
        if not root.left and not root.right: return True
        # 이건 예외 처리 해줬는뎅 ㅠㅠ
        if not root.left or not root.right: return False
        # 트리는 기본적으로 깊이 탐색인듯 
        def dfs(l, r):
            # 왼쪽 오른쪽 둘다 있어야함
            if l and r:
                # 두 값이 똑같은지 확인
                if l.val == r.val:
                    # 똑같으면 다음 검색을 실행 각자 노드는 상반 관계를 확인 하기때문에 한쪽은 left 한쪽은 right로 검색
                    return dfs(l.left, r.right) and dfs(l.right, r.left)
                else:
                    return False
            # 둘다 없는건 괜찮은데 하나 만 없다면 트리가 상반 되어있지않음
            elif l or r: return False
            return True
                
        return dfs(root.left, root.right)