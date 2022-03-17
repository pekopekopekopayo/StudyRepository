# 정수 배열과 삭제 값을 입력값으로 받는다.
# 정수 배열의 참조를 변경하지말고 그 값을 삭제하고 삭제한 배열의 길이를 반환하라
# 정답 체크 알고리즘은 밑과 같다. nums의 정수 값은 0에서 50의 사이이다.
# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
from ast import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # val과 같은 값은 값은 맨 뒤로 빼는 형식을 생각
        j = len(nums) - 1
        # 중복이 몇번이나 일어났는가를 확인하는 변수
        cnt = 0
        for i in range(len(nums)):
            # val값인 값은 -1로 바꿀것이고 -1이 나오면 모든 삭제가 완료가 된 것이다.
            # i-cnt를 한
            if nums[i-cnt] == -1: break
            if nums[i-cnt] == val:
                nums[i-cnt], nums[j] = nums[j], -1
                j-=1
                cnt += 1
        return len(nums) - cnt