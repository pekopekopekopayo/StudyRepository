# 두 바이너리 값이 담긴 문자열이 입력으로 온다.
# 두 문자열을 바이너리 값으로 더 한 문자열을 반환하라.

# bin으로 쉽게 풀 수 있는 문제였지만 문제를 낸 의도와 다를 것 같아
# 먼저 문자열로 풀어 보았다.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 두 리스트의 요소를 더 하면서 문자열에 추가 시킬 예정이다.
        string = ''
        a = list(a)
        b = list(b)
        carry = 0
        # 두 스택이 다 없어야지 모든 연산이 끝난 것이다.
        while a or b:
            # 결과 값은 항상 초기화.
            result = 0
            # 모든 것을 더 한다.
            if a: result += int(a.pop())
            if b: result += int(b.pop())
            # 만약 전 단계에 캐리가 있다면 캐리 값도 함께 더 해준다.
            if carry: result += 1
            # 2진수의 최댓값은 1이고 현재 값에서 result%2를 해주면 0 1이나온다
            string += str(result % 2)
            # 캐리 연산
            carry = result // 2
        # 마지막 캐리가 남아 있는경우 1을 추가 시켜준다.
        if carry: string += '1'
        # 왼쪽부터 추가를 시켰음으로 배열을 뒤집어 주는 것으로 문자열 반환
        return string[::-1]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 둘다 0b(바이너리 문자열)를 붙여주고 10진수로 변환시킨다.
        # 10진수에서 덧셈을 시킨뒤 다시 바이너리 문자로 바꾸어주고 0b를 제거한다.
        return bin(int('0b'+a, 2) + int('0b'+b, 2))[2:]