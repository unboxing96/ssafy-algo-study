def dfs(graph, v, visited):
    vx, vy = v
    if vx > m-1 or vx < 0 or vy > n-1 or vy < 0:
        return False

    loc = [vx, vy]
    print(loc)
    if loc in graph and :
        graph.remove(loc)
        # print(f'{loc}을 지웠습    니다')
        dfs(graph, vx+1, vy)
        dfs(graph, vx, vy+1)
        dfs(graph, vx-1, vy)
        dfs(graph, vx, vy-1)
        # print(f'배추는 {loc}에 있다')
        return True
    return False


T = int(input())

for tc in range(1, T + 1):
    m, n, k = map(int, input().split())     # 열, 행, 배추 수

    lettuce = [list(map(int, input().split())) for _ in range(k)]
    visited = [False for _ in range(k)]
    # # 지도에 배추 위치 표시
    # graph = [[0 for _ in range(m)] for _ in range(n)]
    # for _ in range(k):
    #     col, row = map(int, input().split())
    #     graph[row][col] = 1

    print(lettuce)
    # 모든 위치에서 dfs
    answer = 0
    for i in range(k):
        if dfs(lettuce, lettuce[i], visited):
            answer += 1
    # if dfs(lettuce, 4, 5):
    #     print('yes')

    print(answer)



'''
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6'''
