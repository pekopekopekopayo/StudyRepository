# https://www.acmicpc.net/problem/2294
import sys

input = sys.stdin.readline
n, target = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [10001] * (target+1)
dp[0] = 0
for coin in coins:
  for i in range(coin, target+1):
    dp[i] = min(dp[i], dp[i-coin]+1)

print(-1 if dp[-1] == 10001 else dp[-1])


# 인덱스를 동전 가치 값은 현재 최소 동전 사용량으로 사용한다.
# (현재 값 - 동전 값 + 1) (현재 값)을 비교한다.
# 위와 같이하면 배열은 동전가치 별 최소 동전량을 추출할수있다.