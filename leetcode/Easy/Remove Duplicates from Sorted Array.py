
# 정렬 된 배열이 입력으로 주어진다. 이 배열 이외 다른 객체를 참조하면 안된다.(이 배열을 참조 중이기 때문에 다른 배열을 참조 할 시 런타임에 영향을 줌)
# 중복된 수를 제거하고 중복 삭제 후 길이를 return하여라
# 예시 input [1,1,2] return 2 result [1,2]가 나와야 한다. 
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }



from ast import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 요소 중복제거
        sort_list = list(set(nums))
        # set으로 배열이 엉망이 되어있을거니 정렬
        sort_list.sort()
        # 첫 인덱스마다 값을 갱신해 주면 된다.
        # sort_list만큼만 하면된다. 왜냐하면 sort_list만큼 밖에 출력을 안하기 때문이다.
        # sort_list 길이를 벗어난 nums는 엉망징창이 되어있을 것 이다.
        for i in range(len(sort_list)):
            nums[i] = sort_list[i]
        # sort_list만큼만 하면된다. 왜냐하면 sort_list만큼 밖에 출력을 안하기 때문이다. <-
        return len(sort_list)
    