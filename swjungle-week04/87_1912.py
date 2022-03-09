## 87 1912 연속합 ()


import sys
input = sys.stdin.readline


n = int(input())
num = list(map(int,input().split()))
dp = [0] * n
dp[0] = num[0]
for i in range(1, n) :
    dp[i] = max(dp[i-1] + num[i], num[i])
print(max(dp))