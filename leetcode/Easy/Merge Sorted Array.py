# 합쳐야 할 한 배열과 합치기 전 길이와 합쳐야 할 배열 그리고 그 배열의 길이가 입력으로 온다.
# 합쳐야 할 배열 뒷 부분에는 초기값은 0으로 되어있다. 앞부분의 0은 숫자 0으로 생각한다.
# nums1의 참조 값을 바꾸지 말고 nums1과 nums2를 합치고 오름차순으로 정렬하라.
# 이때 nums1을 참조하여 정답 체크를 하니 return으로 정렬할 값을 반환 하여서는 안된다. 또한 다른 값을 참조해서도 안된다.
# 예시 request [1,2,3,0,0,0] 3 [2, 5, 6] 3

## 하고 싶은 이야기
# 문제를 효율적으로 풀고 싶었는데 머리가 안돌아가서 이 문제 푸는데 2시간 이상 걸렸다.
# 지금 코드도 만족스럽지 않다. 
from ast import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 스택 배열에 정렬할 값을 다 담아준다.
        stack = []
        for i in range(m):
            stack.append(nums1[i])
        for i in range(n):
            stack.append(nums2[i])
        # 그 배열을 정렬한다.
        stack.sort()
        # 정렬한 그 값들을 순서대로 넣어준다.
        for i in range(m+n):
            nums1[i] = stack[i]