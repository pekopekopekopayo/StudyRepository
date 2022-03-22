# https://programmers.co.kr/learn/courses/30/lessons/12969?language=python3
# x축과 y축을 입력으로 받는다.
a, b = map(int, input().strip().split(' '))
# y축을 기준으로 x번까지 진행하여 별을 찍고 x번 반복문이 끝난다면 한칸 뛰어줍니다.
for i in range(b):
    for j in range(a):
        print("*", end="")
    print("")
