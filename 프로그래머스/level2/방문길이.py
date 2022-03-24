# https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3
from collections import deque
def solution(dirs):
    answer = 0
    # 방문한 곳을 체크 할 리스트 10 * 10의 좌표 평면이 주어진다. 좌표 평면의 y x과 y x축의 선을 방문 하는 형식으로 문제를 품
    vist = [[0] * 21 for i in range(21)] 
    dirs = deque(dirs)
    # 중간 부터 시작
    x = 10
    y = 10
    while dirs:
        c = dirs.popleft()
        # -2 + 2를 조건식을 건 이유는 한 칸은 좌표의 선 방문을 위해서 이다.
        # 똑같은 코드가 반복되니 추 후 수정요함
        if c == 'U' and y - 2 > - 1:  
            y -= 1
            if not vist[y][x]:
                answer += 1
                vist[y][x] = 1
            y -= 1
        elif c == 'D' and y + 2 < 21: 
            y += 1
            if not vist[y][x]:
                answer += 1
                vist[y][x] = 1
            y += 1
        elif c == 'L' and x - 2 > 21: 
            x -= 1
            if not vist[y][x]:
                answer += 1
                vist[y][x] = 1
            x -= 1
        elif c == 'R' and x + 2 < 21: 
            x += 1
            if not vist[y][x]:
                answer += 1
                vist[y][x] = 1
            x += 1
    return answer