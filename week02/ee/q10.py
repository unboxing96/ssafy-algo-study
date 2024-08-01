# 자물쇠와 열쇠

# 포기합니다~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 모르겠습니다~~~~~~~~~~~~~~~~~~~~~~

def solution(key, lock):
    answer = True

    # key(M x M)
    # lock(N x N)
    N = len(lock)
    M = len(key)

    # # 확장
    # extended_size = N + 2 * (M - 1)
    # extended_lock = [[0] * extended_size for _ in range(extended_size)]
        
    # # 확장된 자물쇠 중앙에 원래 자물쇠 복사
    # for i in range(N):
    #     for j in range(N):
    #         extended_lock[i + M - 1][j + M - 1] = lock[i][j]

    for _ in range(4):
        key = rotation(key, M)
        answer = can_open(key, lock, N)
        for dx in range(-N//2, N//2+1):
            for dy in range(-N//2, N//2+1):
                key = move(key, M, dx, dy)
                answer = can_open(key, lock, N)
                if answer:
                    return answer

    return answer

# key 회전 함수
def rotation(arr, size):
    new_arr = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            new_arr[i][j]=arr[size-1-j][i]
    return new_arr


def move(arr, size, dx, dy):
    new_arr = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i+dy < size and i+dy >= 0 and j+dx < size and j+dx >= 0:
                new_arr[i][j] = arr[i+dy][j+dx]
        
    return new_arr

def can_open(key, lock, size):
    for i in range(size):
        for j in range(size):
            lock[i][j] += key[i][j]
            if lock[i][j] != 1:
                return False
    return True


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], 
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))  # True
