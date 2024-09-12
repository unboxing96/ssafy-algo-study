from collections import deque
Test = int(input())
for tc in range(1, Test + 1):
    n = int(input())
    # 계산하기 편리하도록 인접행렬로 구현
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    ti = list(map(int, input().split()))
    indegree = [0]*(n+1)

    # 각 행렬에 진입차수와 그래프정보 입력
    for i in range(n):
        for j in range(i+1, n):
            graph[ti[i]][ti[j]] = 1
            indegree[ti[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 그래프에서 순위 바꾸기
        if graph[a][b]: # 모순되거나 순위 알수없을 땐 그래프에 1표시가 있을 것임
            graph[a][b] = 0
            graph[b][a] = 1
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = 1
            graph[b][a] = 0
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    cycle = False # 사이클이 돈다면 impossible
    same = False # 순위 알수 없을 경우(순위 같을 경우) '?' 출력
    lst = []

    for i in range(n):  # n개노드이므로 n만큼만, 정상적 일 때도 마지막 n번째 출력했을 때 큐 비어있어도 cycle True안됨
        if len(q) >= 2:
            same = True
            break
        if len(q) == 0:
            cycle = True
            break
        now = q.popleft()       # 정상적일 때는 굳이 q로 구현안해도 되긴 함, 하나씩만 덱안에 있을 것이므로
        lst.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif same:
        print('?')
    else:
        for i in lst:
            print(i, end=' ')
        print()