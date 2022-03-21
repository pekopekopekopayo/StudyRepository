# 정렬된 두 링크 노드가 있습니다.
# 두 노드를 합쳐서 정렬한 값을 반환해라
# 노드의 -100에서 100사이이다. 
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 최소값의 노드
        head = ListNode(-101)
        # 노드 참조 용 변수
        midle = head
        while list1 and list2:
            # list1 list2를 비교 하고 작은 노드를 midle의 다음 값으로 넣는다
            if list1.val < list2.val:
                midle.next = list1
                list1 = list1.next
            else:
                midle.next = list2
                list2 = list2.next
            midle = midle.next
        
        # 만약에 끝났다면 list1 이나 list2가 남아 있을수도 있다. 나머지는 현재 값 보다 모두 큰 값이므로 현재 값에서 추가 시켜준다.  
        if list1:
            midle.next = list1
        elif list2:
            midle.next = list2
        # midle은 참조 용 노드이기 때문에 맨 처음 값을 가지는 head를 반환 한다.
        return head.next