# 여러 문자열이 담긴 배열이 입력으로 온다.
# 이때 최대 접두사를 찾고 최대 접두사를 반환 하여라
from collections import deque

from ast import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 만약 한가지의 문자열만 온다면 그것 자체가 접두사가 된다.
        if len(strs) == 1: return strs[0]
        # 문자열의 길이대로 정렬은 한다. 이것으로 길이가 제일 큰 문자열만 오게 된다.
        # 길이가 제일 큰 문자열을 기준으로 탐색을 시작한다.
        strs.sort(key=lambda x: len(x))
        long_string = strs.pop()
        for i in range(len(long_string), -1, -1):
            # 길이가 제일 큰 문자열을 뒷 부분을 하나 하나 빼가는 형식으로 진행 하고 모든 값이 전부 일치 하였을때 현재 문자열을 반환 하나라도 틀릴경우에는 탐색을 종료 후 재탐색을한다
            target = long_string[:i]
            switch = True
            for string in strs:
                if not target in string[:i]: 
                    switch = False
                    break
            if switch: return target
        # 만약에 하나도 없을 경우에는 빈 문자열을 반환한다.
        return ""
        