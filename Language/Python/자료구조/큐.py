# 큐를 사용하려면 큐 자료구조를 불러와야한다.
from queue import Queue
# 큐는 아래와 같은 방법으로 적용가능하다.
que = Queue()

# 큐는 스택과는 다르게 삽입한 순서대로 출력이 가능합니다.(선입선출)

for i in range(5):
  que.put(i)

for _ in range(5):
  print(que.get())