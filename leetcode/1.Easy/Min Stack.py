# 밑과 같은 동작을 하는 클래스를 생성하여라
# Your MinStack object will be instantiated and called as such:
# obj = MinStack() 스택 생성
# obj.push(val) 스택 push
# obj.pop() 스택 pop
# param_3 = obj.top() 스택의 최상단 요소
# param_4 = obj.getMin() 스택의 최솟 값
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
