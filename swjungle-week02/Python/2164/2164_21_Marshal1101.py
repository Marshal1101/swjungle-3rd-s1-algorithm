## 2164 21 ์นด๋2 (์๋ฃ)
from collections import deque
import sys

n = int(sys.stdin.readline().strip())

result = deque()
for i in range(n, 0, -1):
    result.append(i)

def card():
    i = n
    while i > 1:
        result.pop()
        i -= 1
        x = result.pop()
        result.appendleft(x)
    print(result[0])

card()