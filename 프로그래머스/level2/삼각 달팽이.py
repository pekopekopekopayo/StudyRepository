# https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3

def solution(n):
    # 피라미드 형태의 배열을 만들어 준다.
    answer = [[0] * i for i in range(1, n+1)]
    # 값을 하나씩 하나씩 넣어줘야하므로 카운터 변수를 하나 생성
    cnt = 0
    # y축으로 먼저 시작해서 내려가기 때문에 y만 -1로 설정해준다.
    y, x = -1, 0
    # n이 0이 되면 로직은 종료 된 것이다.
    while n > 0:
        # n만큼 밑쪽 탐색
        for _ in range(n):
            cnt += 1
            y += 1
            answer[y][x] = cnt
        # 한번 탐색이 끝날때마다 1씩 거리가 좁아짐으로 n - 1
        n -= 1
        # n만큼 오른쪽 탐색
        for _ in range(n):
            cnt += 1
            x += 1
            answer[y][x] = cnt
        # 한번 탐색이 끝날때마다 또 탐새 거리가 1씩 줄어드니 n - 1
        n -= 1
        # 좌상 탐색 
        for _ in range(n):
            cnt += 1
            x -= 1
            y -= 1
            answer[y][x] = cnt        
        # 한번 끝날때 마다 또 탐색 거리가 좁아지니깐 n - 1
        n -= 1
    # 마지막으로 모든 배열을 합치면된다.   
    return sum(answer, [])