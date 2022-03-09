## 90 2579 계단 오르기 (참조, https://pacific-ocean.tistory.com/149)


import sys


input = sys.stdin.readline


n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])


# s로 점수 리스트를 받아주고, dp리스트는 점수의 합을 저장하는 리스트이다.
# dp리스트의 첫번째에는 당연히 s리스트 첫번째 점수가 들어가고,
# dp[1]에는 s[0] + s[1] 즉, 첫번째 점수와 두번째 점수를 합한 값을 넣어준다.
# dp[2]에는 첫번째 계단을 밟고 두 계단을 올랐을때 합과 두번째 계단을
# 밟고 한 계단을 올랐을때 합중 큰 값을 넣어준다.
# 마지막 계단은 꼭 밟아야 하므로
# 1. 마지막 계단의 전 계단을 밟은 경우와
# 2. 마지막 계단의 전 계단을 밟지 않은 경우가 있다.
# 그러므로 dp[i]에는 dp[i - 3] + s[i] + s[i - 1]와 dp[i - 2] + s[i] 이 들어갈 수 있다.
# 이 두 값중에서 큰 값을 넣어준다.