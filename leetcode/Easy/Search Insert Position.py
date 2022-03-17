
# 정렬 된 배열과 검색 할 정수를 입력으로 받는다.
# 검색 값이 배열 안에 있다면 인덱스를 없다면 추가 한 후 인덱스를 반환하여라

# 생각나는 것이 두개가 있어서 두개로 풀어보았다.

from ast import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 스택을 사용 
        while nums:
            # 맨끝값과 타겟 값을 비교 하고 타겟이 크다면 타겟과 같은 값은 배열에 없다는 것이므로 현재 배열 길이를 배출
            # 같다면 지금 배열 길이-1을 하여(index는0부터 시작한다.) 반환
            # 타겟이 작다면 nums의 배열도 같이 줄여준다.
            if nums[-1] < target: return len(nums)
            elif nums[-1] == target: return len(nums) - 1
            nums.pop()
        return len(nums)

from collections import deque
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 데큐를 사용한 방식이고 솔직히 위와 비슷하다.
        nums = deque(nums)
        index = 0
        while nums:
            if nums[0] >= target:
                return index
            index += 1
            nums.popleft()
        return index