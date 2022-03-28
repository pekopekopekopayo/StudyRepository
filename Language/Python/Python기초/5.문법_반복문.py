# 파이썬의 for 반복문은 다음과 같다.

# for (int i = 1; i < 5; i++){
  
# }
for e in range(5):
  print(f"0부터~4까지 현재는 {e+1}번째 반복문을 실행 중 입니다.")

for e in range(1,5):
  print(f"1부터~4까지 현재는 {e}번째 반복문을 실행 중 입니다.")

for e in range(1, 6, 2):
  print(f"1부터~6까지 현재는 {e}번째 반복문을 실행 중 입니다.")

# range는 범위를 뜻한다.
# 인자가 하나 일 경우 range(5) 5번 반복문을 실행 하겠다. 카운터는 1씩 증가 시키겠다. 0 ~ 4 
# 인자가 두개 일 경우 range(1, 5) 1이 5가 될 때 까지 반복문을 실행 시키겠다. 카운터는 1씩 증가 시키겠다. 1 ~ 4
# 인자가 3개 일 경우 range(1, 6, 2)1이 6이 될 때 까지 반복문을 실행 시키겠다. 카운터로 숫자를 2씩 증가 시키겠다.   1, 3, 5

# 이중으로 반복문을 사용을 하면 첫번째 for의 반복횟수 * 두번째 for의 반복횟수 만큼 반복된다.
# 밑의 반복문은 첫번째 반복문 8번 두번째 반복문 9번이므로 72번 반복하게 된다.
for i in range(2, 10):
  for j in range(1, 10):
    print(f"{i} * {j} = {i * j}", end='  ')
  print()


# 파이썬의 while 반복문은 다음과 같다.

start = 0
end = 5
# 조건이 거짓이 될 경우 반복문은 종료 된다.
while start < end:
  start += 1
  print(f"현재는 {start}번째 반복문을 실행 중 입니다.")

# 조건이 거짓이 안되는 경우는 무한루프에 빠져든다.
while start < end:
  print(f"현재는 {start}번째 반복문을 실행 중 입니다.")

# break라는 명령어를 통하여 강제 종료 시킬수있다.

start = 0
end = 5
while True:
  start += 1
  print(f"현재는 {start}번째 반복문을 실행 중 입니다.")
  if start >= end: break

  
  
# 문제: 
# n은 1이상의 수를 입력 받는다.
# 길이가 n인 정 사각형을 출력 시켜라.

# input
# 2
# output
# **
# **

# input
# 4
# output
# ****
# ****
# ****
# ****
