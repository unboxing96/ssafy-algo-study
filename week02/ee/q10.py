# 자물쇠와 열쇠

# 포기합니다~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 모르겠습니다~~~~~~~~~~~~~~~~~~~~~~

def solution(key, lock):
    answer = True

    # key(M x M)
    # lock(N x N)
    N = len(lock)
    M = len(key)

    if can_open(key, lock, N):
        answer = True 
    else:
        for _ in range(4):
            rotation(key, M)
            answer = can_open(key, lock, N)
            if answer:
                return answer
            for dx in range(-N//2-1, N//2+1):
                for dy in range(-N//2-1, N//2+1):
                    move(key, M, dx, dy)
                    answer = can_open(key, lock, N)
                    if answer:
                        return answer

    return answer

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

def can_open(key, lock, size):
    for i in range(size):
        for j in range(size):
            lock[i][j] += key[i][j]
            if lock[i][j] != 1:
                return False
    return True


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], 
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))  # True
