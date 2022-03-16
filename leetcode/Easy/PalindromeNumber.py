# 문자열을 뒤집었을때 같은 숫자인가를 확인하는 프로그램
class Solution:
    def isPalindrome(self, x: int) -> bool: 
        return str(x) == str(x)[::-1]
            