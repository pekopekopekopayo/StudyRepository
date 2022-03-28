# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def dfs(self, index, string):
        # 인덱스를 초과할 경우 정지 그리고 만든 string값을 answer에 삽입
        if index == len(self.s): 
            self.answer.append(string)
            return
        # 7 8 9일 경우에는 각각 경우의 수가 틀리므로 따로 로직처리            
        number = int(self.s[index])
        it = 4 if number == 7 or number == 9 else 3
        s_n = 1 if number > 7 else 0
        # 3번 또는 4번을 실행 재귀
        for i in range(it):
            t = string + chr(97 + i + s_n + (number-2 ) * 3) 
            self.dfs(index+1, t)
            
    def letterCombinations(self, digits: str) -> List[str]:
        # 정답
        self.answer = []
        self.s = list(digits)
        if not self.s: return []
        self.dfs(0, '')
        return self.answer
    