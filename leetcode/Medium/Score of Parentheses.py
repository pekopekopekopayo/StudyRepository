# 괄호 문자열이 입력으로 온다.
# ()는 1의 값이고 (())는 2의 값이고 ((()))는 4의 값이다 중첩 괄호는 1 2 4 8.... 으로 값을 같는다.
# (()()) 와 같은 경우에는 2*(1+1)가 된다.
# 괄호의 값을 반환하라 


# 코드설명 
# (을 발견하면 중첩 괄호의 값을 만든다.
# 곱셈을 해야하는데 중첩 괄호를 체크하고 곱해줘야하는데 여간 까다로운게 아니다.
# 그러므로 *를 /로 상쇄시키는 코드를 작성했다. (((())(()))) 과 같은경우는 식으로 생각 하면 3중첩 괄호문이므로 4(2 + 2) 가 된다.
# 식은 곧 4 * 2 + 4 * 2 이다.
# 처음 괄호가 열려있을 때 2곱셈을 해주고 닫는 문장이 나왔을때 상쇄 시키는 코드를 작성하였다.  
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        answer = 0
        result = 1
        for i in range(len(s)):
            if s[i] == '(':
                result *= 2 
            elif s[i] == ')':
                result //= 2
                if s[i-1] == '(':answer += result
        return answer
                