# 정수 배열이 입력으로 온다.
# 정수 배열에 마지막 값에 +1을 하였을때 정수 배열을 반환하라.
# request [9] answer = [1, 0]

from ast import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      # 맨뒤 숫자가 9가 아니라면 캐리가 일어나지 않는다.
        if digits[-1] != 9:
            digits[-1] += 1
        # 9인경우 캐리를 시켜준다.
        else:
            digits[-1] = 0
            carry = 1
            for i in range(len(digits)-2,-1,-1):
                if carry and digits[i] == 9: 
                    digits[i] = 0
                else:
                    digits[i] += carry
                    carry = 0
            # 만약에 carry가 0이 아닌경우는 맨 앞자리 캐리가 일어나지 않았기 때문에 맨 앞자리에 1을 추가 해준다.
            if carry: digits.insert(0,1)
        return digits