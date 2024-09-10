# 백준 10159번 저울

n = int(input())  # 물건 개수
m = int(input())  # 비교결과 개수

floyd = [[0 for _ in range(n + 1)] for _ in range(n + 1)]  # 0 : 대소관계 알 수 없음

for _ in range(m):
    heavy, light = map(int, input().split())
    floyd[heavy][light] = 1

for i in range(1, n + 1):
    floyd[i][i] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not floyd[i][j]:
                floyd[i][j] = floyd[i][k] and floyd[k][j]  # 자신보다 가벼운 물건 표시하기

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if floyd[i][j]:
            floyd[j][i] = 1  # 자신보다 무거운 물건 표시하기

for i in range(1, n + 1):
    print(n - sum(floyd[i]))
