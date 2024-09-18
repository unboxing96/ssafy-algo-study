import sys
sys.stdin = open('input.txt')

"""
2040 이민혁 > N개의 행성 이루어짐.

A(X Y Z) B(X Y Z) 터널 연결 비용은
비용 = min(|xa -xb|, |ya-yb|,|za-zb|)

터널을 모두 연결하려함. 터널 연결시 최소 비용?

"""

def find_parent(parent, x):
    # x가 속한 집합의 대표자 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 경로압축
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a) # 각각 대표자 찾고
    b = find_parent(parent, b)

    # 사이클이 생기지 않게 간선을 선택해야됨.
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



# 행성의 개수
N = int(input())
location = []
parent = [0] * (N+1) # 부모 테이블 초기화

edges = []
result = 0

for i in range(1, N+1):
    parent[i] = i

for i in range(N):
    x,y,z = map(int, input().split())
    location.append((x, y, z, i)) # 좌표 함께 저장

for i in range(3):
    location.sort(key=lambda planet: planet[i])

    # 인접한 간선 정보 추출하여 처리
    for j in range(1, N):
        # 비용순으로 처리하기
        cost = abs(location[j][i] - location[j - 1][i]) # min(|xa -xb|, |ya-yb|,|za-zb|)
        edges.append((cost, location[j][3], location[j - 1][3])) # 거리, 행성 1 행성 2

# 간선을 비용순으로 정렬
edges.sort()

for cost, u, v in edges:
    # 사이클이 발생하지 않으면 집합에 넣기
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += cost

print(result)