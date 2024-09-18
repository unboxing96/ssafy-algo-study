# 백준 2887번 행성 터널

def find_set(x):  # 대표자 찾기
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):  # union
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


import sys
input = sys.stdin.readline

n = int(input())
x_sorted, y_sorted, z_sorted = [], [], []
for i in range(n):
    X, Y, Z = map(int, input().split())
    # 각 축의 좌표와 노드번호 저장하기
    x_sorted.append([X, i])
    y_sorted.append([Y, i])
    z_sorted.append([Z, i])

# 오름차순으로 정렬
x_sorted.sort()
y_sorted.sort()
z_sorted.sort()

edges = []
for i in range(n - 1):
    # 각 축의 간선 저장(정렬을 통해 가장 가까운 거리의 간선만을 저장)
    edges.append([x_sorted[i][1], x_sorted[i + 1][1], abs(x_sorted[i][0] - x_sorted[i + 1][0])])
    edges.append([y_sorted[i][1], y_sorted[i + 1][1], abs(y_sorted[i][0] - y_sorted[i + 1][0])])
    edges.append([z_sorted[i][1], z_sorted[i + 1][1], abs(z_sorted[i][0] - z_sorted[i + 1][0])])

# 가중치 작은 순으로 모든 간선 정렬하기
edges.sort(key=lambda x: x[2])

parents = [x for x in range(n)]     # 각 노드의 부모 노드
cnt = 0
sum_cost = 0    #

# Kruskal
for v1, v2, cost in edges:
    if find_set(v1) != find_set(v2):
        cnt += 1
        union(v1, v2)
        sum_cost += cost
        if cnt == n - 1:    # n-1개의 간선 완성 시 종료
            break

print(sum_cost)
