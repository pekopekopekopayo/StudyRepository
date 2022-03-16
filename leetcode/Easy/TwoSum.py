class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        while nums:
            tmp = nums.pop()
            for i in range(len(nums)+1):
                if tmp == target:
                    return [i-1, len(nums)] 
                elif tmp > target: break
                tmp += nums[i]