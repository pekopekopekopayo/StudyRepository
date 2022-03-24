# 이번 단원은 파이썬의 특징이 나오는 단원이다.
# 파이썬의 조건문은 괄호를 열지 않으며 시작은 ':'으로 시작한다.

# 한줄로 if 문 작성이 가능하다. 
if True: print('hello world')

# 파이썬은 조건문에 괄호를 사용하지 않기 때문에 인덴트(줄 맞춤)으로 범위를 조절한다.

if True:
  print('hello world')


# 밑과 같은 경우는 Syntaxerror가 발생 된다.
# if True:
# print('hello world')

# 파이썬은 삼항 연산을 지원하지 않는다. 하지만 비슷한 기능은 밑과 같이 사용한다.
# 이때 if앞에는 ':'을 붙히지 않는다.

answer = 'hello' if True else 'world'
print(answer)
answer = 'hello' if False else 'world'
print(answer)


# 문제를 하나 풀어보자 숫자 n이 입력으로 들어온다.
# Peko는 n이라는 숫자가 홀수인가 짝수인가를 모른다.
# n이 짝수이면 '짝수'를 n이 홀수라면 '홀수'를 출력하여라.