# 단어와 공백이 포함 될 수도 있는 문자열이 입력으로 온다.
# 맨 끝단 단어의 길이를 반환하라
# 'hello   world  ' 같은경우에는 world가 끝 단어이므로 공백을 제거하고 5의 길이를 가진다.

# 문제를 두방식으로 풀어보았다.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 문자열을 리스트로 함 스택을 사용하여 맨뒤에 것들을 제거하는 방식으로 문제를 풀 것 이다.
        s = list(s)
        # 문자열이 비어 있는 예외가 있을수도 있으므로 0값으로 반환
        if not s: return 0
        # 맨 뒤 공백을 지워준다.
        while s[-1] == ' ': s.pop()
        # 모두 공백일 경우 에러가 날 가능성이 있다. 그러므로 한번더 체크
        if not s: return 0
        # 맨 뒷자리는 공백이 없고 문자가 있을 것이다. 그러니 몇개의 문자가 있는지 카운팅한다.
        # 공백이 오거나 스택이 비었을 경우는 맨뒤의 문자를 다 읽었다는 뜻이 된다.
        cnt = 0
        while s and s[-1] != ' ':
            cnt += 1
            s.pop()
        # 카운팅 된 수 출력
        return cnt

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 시작 지점과 끝지점의 index로 푸는 방법
        # 시작은 0이고 끝은 문자열 마지막 자리 이다.
        idx_s, idx_e = 0, len(s)
        # 마지막 자리 부터 체킹을 한다. 문자가 있으면 마지막 문자열의 index를 저장하고 반복문을 정지한다.
        for i in range(idx_e-1, -1 ,-1):
            if s[i] != ' ': 
                idx_e = i + 1
                break
        # 마지막 자리 index는 문자의 끝 부분이 된다. 이제 공백이 나올때 까지 또는 문자를 다 읽을때까지 반복한다.
        # s값은 초기 값이 0이므로 다른 예외 사항은 발생되지 않는다. 
        for i in range(idx_e - 1, -1, -1):
            if s[i] == ' ':
                idx_s = i + 1
                break
        # 끝부분과 시작부분을 뺌으로써 끝 문자열의 길이를 구할수있다. 
        return idx_e - idx_s