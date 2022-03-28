# 파이썬이 제공하는 배열형 자료형은 list이다. 배열 요소의 참조 삽입 갱신 삭제가 가능하다. 
# 다른 타입의 데이터도 같이 담을 수 있다.
int_list = [1, 2, 3, 4, 'hello']
print(int_list)
# 인덱스 참조도 가능하다. 인덱스는 0 ~ len(int_list) - 1 이다. `이때 len은 배열의 길이를 반환해주는 메소드 이다.` 
print(len(int_list))
print(int_list[0], int_list[1], int_list[2], int_list[3], int_list[4])

# 초과한 인덱스 범위를 참조 할 경우 에러가 발생한다.
# print(int_list[len(int_list)])

# list의 반복문은 아래와 같이 많이 사용한다.

# 배열 요소를 하나씩 참조 한다.
for e in int_list:
  print(e)

# 인덱스를 활용하여 참조하는 방식
for i in range(len(int_list)):
  print(int_list[i])

# 문제:
# 공백을 둔 문자열 숫자들이 주어진다.
# 문자열의 모든 숫자의 합계를 구하여라  
# hint* split()는 문자열의 메소드이다. 인수 값을 기준으로 문자열 배열을 생성 시켜준다.
print("강아지 고양이 犬 ネコ Dog Cat".split(' '))

# input
# "1 2 3 4 5"
# output
# 15

# Stack이란
# Stack이란 데이터를 push(삽입) pop(배출) 가능한 자료구조 이다. Stack은 맨 마지막에 넣은 요소가 맨 처음으로 pop(배출)되며 맨 처음으로 삽입 된 요소가 제일 늦게 pop(배출)이 된다.
# 파이썬의 list도 Stack의 성질을 가지고 있다.

stack = []
for i in range(5):
  stack.append(i) # 파이썬에서는 push 명령어가 append 이다.
print(stack)


new_stack = []
for i in range(5):
  new_stack.append(stack.pop()) # 빈 배열일때 pop()을 할 경우 에러가 발생 된다.
# 마지막에 넣은값이 처음 배출되므로 두 list가 있을경우 배열을 뒤집을수도 있다.
print(new_stack)
print(stack)

# while의 경우
stack = ['않써요','사투리','서울 사람이여서','저는']
while stack: # 파이썬은 빈 list은 False값으로 취급한다.
  print(stack.pop(), end=' ')

# 문제: 
# 한 숫자N과 공백을 둔 문자열 숫자들이 주어진다.
# 이때 공백을 둔 문자열의 숫자를 배열로 만들고 그 배열에 숫자N이 포함되어 있을 경우 N을 삭제시킨 
# 오름 차순으로 정렬 된 배열을 출력하여라
# hint* list.sort()를 하면 배열을 정렬 할 수 있다.
# hint* list.sort(reverse=True) 내림차순
# 
# input
# "1"
# "1 2 3 4 5"
# output
# [2,3,4,5]
#
# input
# "3"
# "1 3 2 3 4 5 3"
# output
# [1,2,4,5]

# https://www.acmicpc.net/problem/10828 <- 자신이 있으면 풀어 볼 것
