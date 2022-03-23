# https://programmers.co.kr/learn/courses/30/lessons/87946?language=python3
# 술마시고 풀어서 조금 코드가 난잡하다. 추후 수정 요함
global answer
answer = 0

def solution(k, dungeons):
  # 탐색한 곳 인지 확인을 해야함으로 vist을 설정 
  vist = [False] * len(dungeons)
  dfs(k, dungeons, 0, vist)
  return answer

def dfs(k, dungeons, cnt, vist):
  # answer을 global로 설정 해놓고 cnt랑 계속 비교를 할 것이다. 아마 이 부분을 좋게 수정 할 수 있을 것 이다. 하지만 술이 됬으므로 패스
  global answer
  answer = max(answer, cnt)
  for i in range(len(dungeons)):
      # 방문 한 곳은 무시해도 괜찮다. 하지만 다시 탐사를 할 수도 있으므로 백트래킹을 해준다.
      if not vist[i]:
          vist[i] = True
          if k >= dungeons[i][0]: dfs(k-dungeons[i][1], dungeons, cnt+1, vist)
          vist[i] = False
    