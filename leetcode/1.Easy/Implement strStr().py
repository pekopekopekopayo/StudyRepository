# 문자열 두개를 입력으로 받는다.
# haystack 문자열안에 needle문자열이 포함되는가를 찾고 needle이 빈 문자열이면 0을 포함이 되지 않으면 -1을 포함이된다면 포함된 인덱스값을 반환하라.

# 정답을4개 제출했다. 정답 시간이 오래 걸렸기 때문이다. 정답 순서는 역순이다.



# 47ms
# 시간이 올래 걸리는 것은 배열을 자르고 배열을 할당하고 문자열과 문자열을 비교 할때라고 생각했다.
# 그것을 최소한으로 하기 위해서 조건을 몇개 더 걸었다. 그러니 확실히 빨라 졌다.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 만약 두 문자열이 같으면 인덱스는 0부터 일치하는 것 이고 needle 빈문자열이면 0이다. 
        if haystack == needle or needle == "": return 0
        l = len(needle)
        # 인덱스가 초과 하지 않게 설정해둔다.
        for i in range(len(haystack)-l+1):
          # 맨처음과 맨끝이 같을때만 체크를 하기로 했다.
            if haystack[i] == needle[0] and haystack[i+l-1] == needle[-1]:
                if haystack[i:i+l] == needle: return i
        return -1

# 159ms
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or needle == "": return 0
        l = len(needle)
        for i in range(len(haystack)-l+1):
            # 현재 위치에서 두 문자열의 앞문자가 같다면 이라는 조건이다.  
            if haystack[i] == needle[0]:
                if haystack[i:i+l] == needle: return i
        return -1
# 483ms
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or needle == "": return 0
        cnt = 0
        while haystack != "":
            # 문자열을 검색하고 하나씩 자른다. 문자열이 없어질때까지 반복 
            if haystack[:len(needle)] == needle: return cnt
            haystack = haystack[1:]
            cnt += 1
        return -1

# 296ms
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or needle == "": return 0
        cnt = 0
        while haystack[cnt:cnt+len(needle)] != "":
            # index를 늘리는 방식으로 문자열을 비교 
            if haystack[cnt:cnt+len(needle)] == needle: return cnt
            cnt += 1
        return -1