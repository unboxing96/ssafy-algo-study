import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) != n: # 결과 순위가 제대로 안 나오면
        print("IMPOSSIBLE") # IMPOSSIBLE
    else:
        for i in result:
            print(i, end=' ')
        print()


for _ in range(T):
    n = int(input())  # 팀의 수 n
    rank = list(map(int, input().split()))
    m = int(input())  # 상대적인 등수가 바뀐 쌍의 수 m

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(n): # 원래 순위 graph에 넣어두기
        for j in range(i + 1, n):
            graph[rank[i]].append(rank[j])
            indegree[rank[j]] += 1

    for _ in range(m):
        a, b = map(int, input().split())

        if a in graph[b]: # 원래 b->a
            graph[b].remove(a) # 삭제하고
            indegree[a] -= 1

            graph[a].append(b) # 순서 바꿔주기
            indegree[b] += 1

        elif b in graph[a]: # 원래 a->b
            graph[a].remove(b) # 삭제하고
            indegree[b] -= 1

            graph[b].append(a) # 순서 바꿔주기
            indegree[a] += 1

    topology_sort()
