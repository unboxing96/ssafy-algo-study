# 문제

# 퀴즈: dfs 함수를 stack으로 구현하여 예시대로 출력하시오
# 조건: 재귀 함수 사용 금지

def dfs_stack(graph, start):
        stack = []
        visited[start] = True
        print(start, end=' ')
        v = start # 현재 정점 표시
        while True:
            for w in graph[v]:
                if visited[w] == False:
                    stack.append(v)
                    v = w
                    print(v, end= ' ')
                    visited[w] = True
                    break
            else:
                if stack:
                    v = stack.pop()
                else :
                    break



##########################    수정금지    ###########################
# 예제 그래프: 인접 리스트로 표현
# 가정1: 노드는 1부터 시작
# 가정2: 오름차순으로 정렬되어 있음
graph = [[], [2, 3], [1, 4, 5], [1, 6], [2], [2, 6], [3, 5]]

n = len(graph)
visited = [False] * (n + 1)

# DFS 실행
dfs_stack(graph, 1)

# 출력 예시
# 1 2 4 5 6 3
###################################################################