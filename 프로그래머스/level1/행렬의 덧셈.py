# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        # 전체 배열 길이 만큼 실행 시켜 한 배열에 넣어야 함으로 배열을 처음에 넣어준다.
        answer.append([])
        for j in range(len(arr1[i])):
            # arr1과 arr2 같은 index에 있는 값을 더한다. 그리고 처음에 push했던 배열에 값을 push한다.
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer