# https://programmers.co.kr/learn/courses/30/lessons/92341?language=python3
from collections import defaultdict, deque
import math
def solution(fees, records):
    answer = []
    # 항상 in out 순서로 오기 때문에 deque 활용
    dic = defaultdict(deque)
    # 일단 번호판 별대로 딕셔너리를 구성 하고 in out시간을 push 한다.
    for record in records:
        record = record.split()
        dic[record[1]].append(record[0])
    # 차 번호판 오름차순 순서 대로 정렬해야하니 키를 정렬하고
    keys = list(dic.keys())
    keys.sort()

    # 정렬된 키대로 반복문을 실행하자
    for key in keys:
        # 처음 시간은 0이고
        time = 0
        while dic[key]:
            # 시작 시간과 종료 시간을 분리해서 시간은 * 60 분은 + 로 해서 계산 한 후 차를 낸다.
            start = dic[key].popleft().split(':')
            if dic[key]: end = dic[key].popleft().split(':')
            else: end = ['23', '59']
            start = int(start[0]) * 60 + int(start[1])
            end = int(end[0]) * 60 + int(end[1])
            time += end - start
        # 그 뒤 계산식에 따라 계산 해준다 만약에 기본요금보다 계산식 요금이 덜 나왔을 경우에는 기본요금을 청구한다.
        result = math.ceil((time - fees[0]) / fees[2]) * fees[3] + fees[1]
        if result < fees[1]: answer.append(fees[1])
        else: answer.append(result)
    # 끝
    return answer