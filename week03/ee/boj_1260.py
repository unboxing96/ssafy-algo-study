# DFS와 BFS

N, M, v = map(int, input().split()) # N: 노드 개수, M: 간선 개수, V: 시작 노드

datas = [list(map(int, input().split())) for _ in range(M)] # 간선이 연결하는 두 노드의 번호

# 인접 행렬 만들기
def adjacency_matrix(datas, N):
    matrix = [[0] * (N+1) for _ in range(N+1)]

    for data in datas:
        i, j = data
        matrix[i][j] = 1
        matrix[j][i] = 1

    return matrix

graph = adjacency_matrix(datas, N)
# for row in graph:
#     print(*row)

###################### DFS #############################

visited = [False] * (N+1) # 방문 처리 저장할 리스트

def dfs(graph, N, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in range(N+1):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, N, i, visited)

dfs(graph, N, v, visited)
print()

####################### BFS ##########################

visited = [False] * (N+1) # 방문 처리 저장할 리스트

from collections import deque

def bfs(graph, N, v, visited):
    queue = deque([v]) # 큐 초기화 => 시작 노드를 큐에 추가
    visited[v] = True # 방문 처리
    while queue: # 큐가 빌 때 까지!
        v = queue.popleft() # 왼쪽부터 꺼낸다
        print(v, end=' ') # 현재 방문한 노드 출력
        for i in range(N+1):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, N, v, visited)

