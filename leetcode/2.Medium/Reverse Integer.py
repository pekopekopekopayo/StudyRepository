# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        # 양수 음수를 판별 x는 절대 값을 가짐
        flag = True if x < 0 else False
        # 문자열 -> 리스트 -> 뒤집기 -> 문자열 -> 정수 
        x = list(str(abs(x)))
        x = x[::-1] 
        x = int(''.join(x))
        # 31비트 이상일 경우 0을 반환
        if x >= 2 ** 31: return 0
        # 음수일 경우에는 -를 표시해줌
        if flag: x *= -1 
        # 3 반환
        return x