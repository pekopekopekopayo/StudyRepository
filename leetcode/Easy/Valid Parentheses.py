# 각각 괄호 () {} [] 를 입력 값으로 받는다.
# 각각의 괄호는 여닫이가 확실하게 되어야한다.
# 이때 입력 값으로 받은 괄호는 올바른 괄호인가를 True False로 반환하라
class Solution:
    def isValid(self, s: str) -> bool:
        # 스택을 이용하여 자기의 맨 위쪽요소와 다음 문자열을 판단한다.
        stack = []
        for c in s:
            # 스택이 없다면 괄호가 다 닫힌거임으로 스택을 채워준다.
            if not stack:
                stack.append(c)
                continue
            # 스택의 맨 윗부분과 그 윗부분이 여닫이가 이루어 져 있다면 스택의 맨 윗단계를 제거 그리고 반복 한다.
            if stack[-1] == '(' and c == ')':
                stack.pop()
            elif stack[-1] == '[' and c == ']':
                stack.pop()
            elif stack[-1] == '{' and c == '}':
                stack.pop()
            else:
                stack.append(c)
        # 스택이 있다면 올바르지 않은 괄호 이며 스택이 존재 하지 않는다면 올바른 괄호가 된다.
        return not bool(stack)
            