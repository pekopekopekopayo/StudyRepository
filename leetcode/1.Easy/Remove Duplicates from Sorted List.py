
# 정렬된 리스트 노드를 입력 값으로 받는다.
# 중복을 제거한 리스트노드를 반환하여라
# val값은 -100 =< val >= 100 이다.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 한 노드 만들고
        tmp_head = ListNode(val=-101)
        # 그 노드 참조 할 친구 만들고
        body = tmp_head
        # head 끝 까지
        while head:
            # body와 head의 둘의 값이 같으면 중복 값이므로 틀리면 새로운 노드를 body에 이어주고 body는 새로운 노드 값을 가진다.  
            if body.val != head.val: 
                body.next = ListNode(val=head.val)
                body = body.next
            # 노드 탐색이 끝났으므로 다음 노드를 준비한다..
            head = head.next
        # -101이라는 가중치를 넣어서 리스트노드를 만들었기 때문에 next한 값이 실제 중복이 없는 정렬된 리스트 노드가 된다.
        return tmp_head.next