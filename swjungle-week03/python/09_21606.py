## 09 21606 아침 산책 (73점)
# DFS 사용
# 1 ~ N개 정점에서 i 와 i+1 사이에 모두 간선 있을 때 뭔가 문제발생???

# 수학
# 그래프 이론
# 그래프 탐색
# 트리
# 깊이 우선 탐색
# 조합론


import sys
input = sys.stdin.readline

n = int(input())

inside = ['실내1 야외0'] + list(map(int,input().strip()))

edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)


def DFS(start):
    visited = [False] * (n+1)
    is_inside = False
    if inside[start] == 0:
        is_inside = True
    stack = [start]
    visited[start] = True
    total = 0
    while stack:
        count_in = 0
        count_out = 0
        node = stack.pop()
        for adj in edge[node]:
            if visited[adj] == False:
                if inside[adj] == 1:
                    if is_inside:
                        count_in += 1
                    else:
                        count_out += 1
                else:
                    visited[adj] = True
                    stack.append(adj)            
        total += count_in + count_out * (count_out-1)
    return total

total = 0
for i in range(1, n+1):
    total = total + DFS(i)
print(total)