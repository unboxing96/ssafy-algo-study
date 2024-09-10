# 10159 저울
import sys
sys.stdin = open('input.txt')

"""
무메가 서로 다른 N개의 물건 존재.
각 물건은 1 ~ N까지의 번호가 매겨져 있음.
어떤 것이 무거운것인지 측정한 결과표 있음.
비교 결과가 모순되는 입력은 x
물건의 개수N, 
비교 결과 주어지면 각 물건에 대해서 비교 결과를 알 수 없는 물건의 개수 출력.
모든 노드에서 > 모든 방향으로 체크 가능해야함.

어떻게 해야 비교 가능함을 알 수 있니?
1 : 5,6, 2개 > 즉 대소 비교가 안되었다 : 그래프상으로 연결되지 x 근데 N이 200개임.
2 : 5, 6, 2 개 > 
3 : 5, 6,  2 개
4 : 0 
5 : 3
6 : 3

결론:
- 모든 모드에서 모든 방향으로 체크 가능해야하며, O(N ** 3) > 모든 노드체크 : 플로이드워셜
    - 모든 노드 찾는 이유: 각 물건에 대해서 모두 출력이 필요함.
- 길찾을때 갈 수 없는 방향에 존재하는것을 출력하면 정답임.  > 둘다 INF임을 체크하면됨
"""


# 물건 개수
thing_cnt = int(input())
measured_cnt = int(input())  # 2천개까지 들어옴.
measured_list = [list(map(int, input().split())) for _ in range(measured_cnt)] # 앞에 물건이 더 무거움 # [[1, 2], [2, 3], [3, 4], [5, 4], [6, 5]]

# 플로이드 워셜 알고리즘
INF = int(1e9)

graph = [[INF] * (thing_cnt+1) for _ in range(thing_cnt+1)]

# 자기 자신에게 가는 비용을 0으로 초기화
for a in range(1, thing_cnt+1):
    for b in range(1, thing_cnt+1):
        if a == b:
            graph[a][b] = 0 # 비용은 0으로 설정

# 그래프에 정보를 담아주기. (대소비교된 measured_list활용 하여 연결 체크)
for a, b in measured_list:
    graph[a][b] = 1
    # graph[b][a] = 1

for k in range(1, thing_cnt+1):
    for a in range(1, thing_cnt+1):
        for b in range(1, thing_cnt+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])

# 양쪽 모두 무한이면 없는것임.
for i in range(1, thing_cnt + 1):
    count = 0
    for j in range(1, thing_cnt + 1):
        if graph[i][j] == INF and graph[j][i] == INF:
            count += 1
    print(count)