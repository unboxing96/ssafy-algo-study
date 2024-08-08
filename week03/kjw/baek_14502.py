n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
new_arr = [[0]*m for _ in range(n)]  # 연구소 크기에 맞춰 초기화

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
'''
솔직히 졸려서 머리가 너무 안돌아가서 답지봤어여ㅛ,,,
우선 따라서 해봤는데 전 이렇게 재귀 호출 체계적으로 못합니다
주말에 풀어올릴게요 ㅠㅠㅠㅠㅠㅠㅠㅠ
보기 전 어케어케 해야겠다 구현의 생각은 똑같긴 합니다....그나마..
아아아아아아아강ㅁ랑ㅁ나아앙ㄱ악 오늘은 너무졸려 죄송,,,
'''
def virus(s1, s2):  # dfs로 바이러스를 퍼뜨림
    for k in range(4):
        nx = s1 + dx[k]
        ny = s2 + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if new_arr[nx][ny] == 0:  # 빈 칸일 때만 바이러스 퍼뜨림
                new_arr[nx][ny] = 2
                virus(nx, ny)

def get_score():  # 안전 영역의 크기를 계산하는 함수
    score = 0
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 0:
                score += 1
    return score

max_safe_area = 0

def dfs(count):  # 벽 세우는 조합을 찾는 dfs 함수
    global max_safe_area
    if count == 3:  # 벽을 3개 세운 경우
        # new_arr를 arr로 복사 << 다른방법 있을것같은데 굳이
        for i in range(n):
            for j in range(m):
                new_arr[i][j] = arr[i][j]
        
        # 각 바이러스 위치에서 바이러스를 퍼뜨림
        for i in range(n):
            for j in range(m):
                if new_arr[i][j] == 2:
                    virus(i, j)
        
        # 안전 영역의 크기 계산하여 최대값 업데이트
        max_safe_area = max(max_safe_area, get_score())
        return
    
    # 빈 칸에 벽을 세우는 모든 경우를 탐색
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:  # 빈 칸일 때만 벽을 세울 수 있음
                arr[i][j] = 1  # 벽 세우기
                dfs(count + 1)
                arr[i][j] = 0  # 벽 다시 없애기

dfs(0)
print(max_safe_area)
