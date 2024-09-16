import sys
sys.stdin = open("3665.txt")

# 문제 분석
# 인접 리스트로 순위를 표현한다는 것은 . . .
# 인접 노드와 비교를 한다는 것이다.
# 1등은 나머지 4개와 비교해야 한다. 그래야 확실한 1등이니까. 그것이 왕관의 무게.
# 반면 5등은 4등 노드와 비교하는 것으로 충분하다.
    # 1등의 진입차수를 줄이고, 5등의 진입차수를 늘려, 위상 정렬하기 위함이다.

# 입력
# graph는 현재 노드의 인접 노드를 표현하다. 인접 노드라는 것은 현재 노드의 하위 등수 노드이다.
# in_degrees는 현재 노드의 진입 차수이다. 1등 노드를 가장 먼저 꺼낼 수 있도록 한다.

# 순서 바꾸기
# a, b 입력이 들어오면 상대적인 등수가 바뀐 것이다.
# 예컨대 b > a에서 a > b가 된다.
# a는 인접 노드가 늘어난다. (하위 등수에 b 노드 추가)
# b는 인접 노드가 줄어든다. (하위 등수에 a 노드 제거)
# a의 진입 차수는 1 줄어든다.
# b의 진입 차수는 1 늘어난다.

# 위상정렬
# 한다.

from collections import deque

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if in_degrees[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            in_degrees[i] -= 1
            if in_degrees[i] == 0:
                q.append(i)
    
    return result

T = int(input())
for _ in range(T):
    n = int(input())
    rankings = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    in_degrees = [0] * (n + 1)

    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[rankings[i]].append(rankings[j]) # rankings[i]번 노드에 하위 노드 추가
            in_degrees[rankings[j]] += 1 # rankings[j]번 노드 진입 차수(상위 노드 수) 추가

    # 순서 바꾸기
    isIMPOSSIBLE = False
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[a].append(b) # a는 인접 노드가 늘어난다. (하위 등수에 b 노드 추가)
            graph[b].remove(a) # b는 인접 노드가 줄어든다. (하위 등수에 a 노드 제거)        
            in_degrees[a] -= 1 # a의 진입 차수는 1 줄어든다.
            in_degrees[b] += 1 # b의 진입 차수는 1 늘어난다.
        else:
            graph[b].append(a)
            graph[a].remove(b)
            in_degrees[b] -= 1
            in_degrees[a] += 1


    result = topology_sort()
    if len(result) < n:
        print("IMPOSSIBLE")
    else:
        print(*result)