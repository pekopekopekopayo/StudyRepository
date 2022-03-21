# https://www.acmicpc.net/problem/2293
import sys

input = sys.stdin.readline
n, target = map(int, input().split(' '))
dp = [0 for _ in range(target+1)]
coins = [int(input()) for _ in range(n)]
dp[0] = 1
for coin in coins:
  for now_num in range(coin, target+1):
    dp[now_num] += dp[now_num-coin]
    print(dp)
print(dp[target])
print(dp)


# 동전의 조합 또는 단독으로 target의 값을 몇개 만들수 있는가에 대한 문제
# coin의값 부터 target+1까지 탐색을하고 자기가 만들수 있는수의 인덱스에 값을 보존한다.
# 두번째 이후 부터는 그 배열을 이용해   