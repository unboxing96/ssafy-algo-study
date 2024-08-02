'''
DFS나 BFS로 풀거면 graph를 구현해야함
빈 2차원리스트 만들어놓고 앞선문제처럼 리스트에 추가하고 정렬해서 그래프만들자
dfs든 bfs든 출력해놓고 개수세면 되지않나? 1번컴퓨터 빼고
'''
n = int(input())
m = int(input())
visited = [False] * (n+1)
graph =[[] for _ in range(n+1)] 
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

dfs_list = []

def dfs(graph, visited, start):
    visited[start] = True
    dfs_list.append(start)
    for j in graph[start]:
        if visited[j] == False:
            dfs(graph, visited, j)

dfs(graph, visited, 1)
print(len(dfs_list)-1) # 1번컴퓨터 개수 한개 빼고