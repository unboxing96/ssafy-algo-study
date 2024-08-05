# Dfs와 BFS
import sys
from collections import deque

sys.stdin = open('input.txt')


# DFS, BFS로 탐색한 결과 출력 프로그램 작성.
# 단, 작은것부터 방문. 
# 더이상 방문할 수 없는 경우 종료. 1~n번

## DFS
N, M, V = map(int,input().split()) # 정점의 개수 n / 간선의 개수 m / 정점 번호 v

graph = [[] for _ in range(N+1)]
graph2 = graph


for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a) # 무방향이니 그래프 양쪽으로 간선 추가

for adj in graph: # 정렬해야되는 이유: 탐색 순서의 비일관성이 될 수 있기에 정렬이 필요하다.
    adj.sort()

visited = [False] * (N+1)

graph2 = graph
result1 =[]
result2 =[]
# M 개의 줄에 간선이 연결하는 정점의 번호
# 1 > 2 > 4 > 3 으로 탐색할 거긴함. 그걸 구현해야돼.

def dfs(graph, v, visited) :
    visited[v] = True
    result1.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited) # 재귀 활용

    return(result1)
dfs(graph, V, visited)
print(*result1)


## BFS
# BFS는 큐를 활용하게됨.

def bfs(graph, start, visited):
    #큐 구현을 위해 deque사용!
    queue = deque([start])
    # 현재노드는 방문 처리!
    visited[start] = False # 재활용
    # 큐ㅠ가 빌때까지 진행하기.
    while queue:
        # 큐에서 하나의 원소를 뽑아서 출력하기.
        v = queue.popleft() # 큐 방식이니 왼쪽에서부터 선입 선출!
        result2.append(v)
        # 해당 원소와 연결된 방문하지 않은 원소들 큐에다 넣기 (작은것부터 들어가게)
        for i in graph[v]:
            if visited[i]: # 방문한곳으로 가야 false로 다시 재 체크 가능.!
                queue.append(i) # 큐에 싹다 추가하기!
                visited[i] = False # 방문찍기
    return result2



bfs(graph2, V, visited) # 그래프에서 1번 노드부터 시작할거고
print(*result2)