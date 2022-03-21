# 반복되는 문자가 없는 문자열의 최대길이를 반환하라.

from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 문자가 하나도 없다면 길이가 0이므로 예외 처리
        if s == "": return 0
        # 데큐로 문자를 하나 하나 넣고 같은 문자가 있으면 그 문자를 popleft 방식으로 제거 할 예정
        deq = deque([])
        result = 1
        for c in s:
            if not deq: 
                deq.append(c)
                continue
            if c in deq:
                while deq:
                    if c == deq.popleft():
                        break
            deq.append(c)
            # 저번 상황의 최대 값과 지금 상황의 최대 값을 비교해서 큰 값을 가짐
            result = max(result, len(deq))
        # 큰 값의 문자열의 길이가 반환이됨
        return result
    