# https://programmers.co.kr/learn/courses/30/lessons/12954?language=python3
def solution(x, n):
    # 1부터 x만큼만 반복하고 x를 곱하면 되므로 그에 맞는 반복문 작성
    answer = [x * val for val in range(1,n + 1)]
    return answer