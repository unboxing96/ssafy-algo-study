import sys
from collections import deque

sys.stdin = open('input.txt')

# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어 질 때,
# 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 작성하시오.


# dfs / bfs중 뭘써야할까?

# 깊이 우선 탐색,  둘다 가능하지 않을까?
# 둘다 모두 풀이해보기.
# # 컴퓨터의 수를 출력하는 프로그램 작성

# BFS로 풀기


computer = int(input()) # 노드수 vertex
edge = int(input()) # 간선수

graph = [[] for _ in range (computer+1)] # 노드수보다 1개 추가하여 0번째 인덱스를 사용하지 않을것임.
visited = [False] * (computer+1) #0번재 인덱스는 사용하지 않을것임.
result = []

for i in range(edge): # 각 간선의 연결 방향을 graph에 그래주기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for adj in graph: # 그래프 요소들을 정렬함으로써  dfs, bfs가 잘되도록 체크
    adj.sort()


def bfs(graph, start, visited):
    # 디큐를 사용하여 큐를 구현할것임!
    queue = deque([start])
    visited[start] = True

    while queue:
        next_idx = queue.popleft()
        result.append(next_idx)
        for i in graph[next_idx]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return result

bfs(graph, 1, visited)
print(len(result)-1)





# DFS로 풀기
# computer = int(input()) # 노드수! 100이하인 양의 정수
# edge = int(input())# 간선의 개수! 연결된 컴퓨터 쌍의 수
#
# graph = [[] for _ in range(computer+1)] # 한쌍씩 연결되어있는 컴퓨터 번호의 쌍(노드 노드) 가 입력됨.
# # print(graph) # [[], [], [], [], [], [], [], []] 8개 생성됨.
#
# for i in range(edge): # 각 연결되어있는 간선의 개수만큼 graph에 넣기
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# for adj in graph : # graph의 각각의 요소를 전부 정렬하기
#     adj.sort()
#
# visited = [False] * (computer+1)
# result = []
#
#
# def dfs(graph, start, visited) :
#     visited[start] = True
#     result.append(start)
#
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
#     return result
#
#
# dfs(graph, 1, visited)
#
# print(len(result)-1)