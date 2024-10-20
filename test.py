# import sys
# sys.stdin = open("test.txt")

# def dfs_stack(root):
#     path = [] # 방문한 꼭지점들을 기록한 리스트
#     stack = [root]
    
#     while stack:
#         node = stack.pop() # node : 현재 방문하고 있는 꼭지점
        
#         #현재 node가 방문한 적 없다 -> path에 추가한다.
#         #그리고 해당 node의 자식 node들을 stack에 추가한다.
#         if not visited[node]:
#             visited[node] = True
#             path.append(node)

#             for next in reversed(graph[node]):
#                 if not visited[next]:
#                     stack.append(next)

#     return path


# # TestCase 개수
# T = 1

# # TestCase만큼 반복
# for tc in range(1, T + 1):

#     v, e = map(int, input().split())
#     adj_arr = list(map(int, input().split()))
#     graph = [[] for _ in range(v + 1)]
#     visited = [False] * (v + 1)

#     for i in range(0, len(adj_arr), 2):
#         a, b = adj_arr[i], adj_arr[i + 1]
#         graph[a].append(b)
#         graph[b].append(a)

#     result = dfs_stack(1)
#     print(f'#{tc}', end = " ")
#     print(*result, sep="-")

print(2 / 1)