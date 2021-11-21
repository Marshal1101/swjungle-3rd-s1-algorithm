## 04 1260 DFS와 BFS (구현: 01)
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque
import sys
input = sys.stdin.readline

# 자료구조 - 인접리스트
N, M, V = map(int,input().split())
adjacent = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int,input().split())
    adjacent[v1].append(v2)
    adjacent[v2].append(v1)

# 방문 시 작은 수 먼저 방문하므로, 인접정점 오름차순 정렬
for i in range(N+1):
    adjacent[i].sort()


# 자료구조 - 방문리스트
visited = [False] * (N+1)

# DFS
def dfs(ajacent, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in ajacent[v]:
        if visited[i] != True:
            dfs(ajacent, i, visited)

# BFS
def bfs(ajacent, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in ajacent[v]:
            if visited[i] != True:
                queue.append(i)
                visited[i] = True

dfs(adjacent, V, visited)
print()
visited = [False] * (N+1)
bfs(adjacent, V, visited)