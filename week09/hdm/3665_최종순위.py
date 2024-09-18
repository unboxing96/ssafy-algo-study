import sys
sys.stdin = open('input.txt')

"""
올해 참가팀은 작년에 참가했던 팀과 동일.
ACM - ICPC 대전 
1번부터 n까지 번호가 매겨져 있음. 
작년에 비해 순위가 바뀐 팀의 목록만 발표
순위가 바뀌면 (6 -> 13) 발표.

순위 바뀐 팀의 목록만 주어짐.
올해 순위를 만드는 프로그램?

확실한 올해 순위를 만들 수 없을수도 있고, 일관성이 없는 정보일 수도 있음.

# 등수가 안 바뀔수도 있음.
1등 팀부터 순서대로 출력. 순위 찾을 수 없으면 '?' 출력 데이터 일관성이 없는 경우 순위 x > impossible

"""

# 덱 선언
from collections import deque


def topology_sort():
    result = []  # 알고리즘 수행 결과 담을 리스트
    q = deque()

    # 처음 시작할때는 진입차수가 0 인 노드를 큐에 넣어줘야함. 전부순회하면서.
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        if len(q) > 1:
            return -1
        # 큐에서 원소 꺼내고
        now = q.popleft()
        result.append(now)

        # 연결된 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result  # 순위 담김

T = int(input())

for tc in range(1, T+1):
    # 팀의 수
    n = int(input())
    # 작년에 i등을 한 팀의 번호 / 인덱스 값을 기준으로 높음.
    ti = list(map(int, input().split()))
    # 등수가 바뀐 쌍의 수
    change_cnt = int(input())

    # 모든 노드에 대해서 진입차수 0 초기화
    indegree = [0] * (n+1)
    # 그래프 그려주기 (연결 리스트)
    graph = [[] for i in range(n+1)]


    # 난 이미 정렬된 순위가 있음.
    # 5 4 3 2 1
    for i in range(n):
        for j in range(i + 1, n):
            graph[ti[i]].append(ti[j]) # 앞뒤 비교
            indegree[ti[j]] += 1

    # 이제 바뀐순위 진입차수를 만들어주는것임.
    for _ in range(change_cnt):
        a, b = map(int, input().split())
        # a가 b보다 높아짐.
        if b in graph[a]:
            graph[a].remove(b) # a에서 b로 이동가능하게.
            graph[b].append(a)
            indegree[a] += 1 # a로가는 경로 하나더 생김. 위상 정렬이니.
            indegree[b] -= 1 # a가 b보다 높아져서 b로가는 경로 하나 줄어듬
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[b] += 1
            indegree[a] -= 1


    result = topology_sort()

    if len(result) != n:
        print("IMPOSSIBLE")

    elif result == -1 :
        print("?")

    else:
        print(" ".join(map(str, result)))