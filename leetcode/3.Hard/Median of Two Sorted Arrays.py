# 정렬이 된 두 정수 배열이 입력으로 온다.
# 두 정수 배열을 합쳐서 숫자를 정렬 시키고 중간 인덱스를 참조하여 값을 출력하여라
# 두 정수 배열을 합친 길이가 짝수 일 경우 중간 인덱스의 두 값을 더 하고 나누어 출력하여라

# 예시 
# [1,2], [3] 중간 값은 2
# [1,2,3] [4] 배열을 합치면 [1,2,3,4] 길이가 짝수인 배열이다. 중간 인덱스의 값이 2와 3이 있으니 (2 + 3) / 2 
from ast import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 예외를 피하기 위하여 두 배열을 합치고 정렬을 한다.
        nums3 = nums1 + nums2
        nums3.sort()
        # 길이를 측정하여 홀수인 경우는 중간값을 짝수인 경우는 중간값 두개를 합치고 나누는 로직을 추가 
        l = len(nums3)
        if l % 2:
            return nums3[l//2]
        else:
            return (nums3[l//2] + nums3[l//2-1]) / 2