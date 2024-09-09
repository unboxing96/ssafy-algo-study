def solution(n, s, a, b, fares):

    # 플로이드 워셜 구현
    # 테이블 INF로 초기화
    INF = int(1e9)
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    # 자기 자신 0으로 초기화
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dist[i][j] = 0
    
    # fares 입력 받아 양방향 거리 업데이트
    for fare in fares:
        a_node, b_node, c = fare
        dist[a_node][b_node] = c
        dist[b_node][a_node] = c

    # 플로이드 워셜 알고리즘으로 업데이트
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 다시 노드 개수만큼 반복하여
    # (s -> k -> a + s -> k -> b) 값과 (s -> a + s -> b) 값 중 최소값을 저장
    # 전자를 계산할 때 s -> k는 한 번만 (합승)
    min_dist = int(1e9)
    for k in range(1, n + 1):
        min_dist = min(min_dist, min(dist[s][k] + dist[k][a] + dist[k][b], dist[s][a] + dist[s][b]))

    answer = min_dist
    return answer


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))