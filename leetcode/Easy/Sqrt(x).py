# 정수가 입력으로 들어온다.
# 제곱근을 계산하고 반환하라(소수점은 버린다.)

class Solution:
    def mySqrt(self, x: int) -> int:
      # 너무 간단하다. 그냥 0.5승을 해주면된다.
        x = int(x ** 0.5)
        return x
        