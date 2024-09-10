def BF():
    INF = 1e9
    dist = [INF]*(n+1)
    dist[1] = 0

    for i in range(n):      # 모든 노드를 돌면서 갱신하기
        for t, s, e in paths:
            if dist[e] > dist[s] + t:
                if i == n - 1:  # n번째에 갱신된 경우: 음의 사이클 존재
                    print('YES')
                    return
                dist[e] = dist[s] + t
    print('NO')


TC = int(input())
for tc in range(TC):
    n, m, w = map(int, input().split())

    paths = []

    for _ in range(m):  # 도로 : 무방향
        s, e, t = map(int, input().split())
        paths.append([t, e, s])
        paths.append([t, s, e])
    for _ in range(w):  # 웜홀 : 단방향
        s, e, t = map(int, input().split())
        paths.append([-t, s, e])

    BF()
