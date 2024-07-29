# 문제 분석
# 열쇠는 회전과 이동이 가능하다.
# 회전
    # 하나의 방향으로 90도씩 4번 가능하다.
# 이동
    # key 전체를 이동해야 한다.
    # 각 방향으로 3번씩 이동이 가능하다.
    # 방향이 4개이므로, 총 12가지의 케이스가 있을 수 있다.
# 주어진 배열의 크기가 20밖에 되지 않으므로 완전탐색으로 구현하자.


# 접근
# 회전이야 쉽다.
# 이동이 문제다. N x N 배열이라면 N ** 2만큼 탐색해야 한다.
# 구글링해서 lock 배열을 3배로 확장하면 된다는 아이디어를 얻었다.
# 3배 크기의 배열을 생성하고, 가운데에 lock을 배치한다.
# 배열의 (1, 1)부터 (N, N)까지 탐색하면, 모든 경우의 수를 탐색할 수 있다.

# 회전 함수를 구현하자 rotate90
# lock 배열을 3배로 확장하자 extended_lock
# 회전 방향마다 한 번씩, 총 4번 탐색한다.
    # 확장된 배열을 (1, 1)부터 (N, N)까지 탐색하며,
    # key 배열을 extended_lock 배열에 더해준다.
    # 기존 lock 배열 부분만 탐색하며, 모든 값이 1인지 확인한다. True하면 함수 종료. 아니라면 빠져나온다.
    # key 배열을 extended_lock 배열에서 다시 빼준다. (백트래킹)
# 중간에 탈출하지 못 하고 반복이 끝나면 False

def solution(key, lock):
    n = len(lock)
    extended_lock = [[0] * (n * 3) for _ in range(n * 3)] # 확장된 배열 생성
    for i in range(n):
        for j in range(n):
            extended_lock[i + n][j + n] = lock[i][j]
            
    for _ in range(4): # 회전 방향마다 한 번씩, 총 4번 탐색
        key = rotate90(key)
        for x in range(1, n * 2):
            for y in range(1, n * 2):
                add_key_to_extended_lock(x, y, key, extended_lock)
                if check(n, extended_lock):
                    return True
                subtract_key_to_extended_lock(x, y, key, extended_lock)
    return False


def rotate90(arr):
    n = len(arr)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = arr[i][j]
    return rotated


def add_key_to_extended_lock(x, y, key, extended_lock):
    n = len(key)
    for i in range(n):
        for j in range(n):
            extended_lock[i + x][j + y] += key[i][j]
            

def subtract_key_to_extended_lock(x, y, key, extended_lock):
    n = len(key)
    for i in range(n):
        for j in range(n):
            extended_lock[i + x][j + y] -= key[i][j]


def check(n, extended_lock):
    for i in range(n):
        for j in range(n):
            if extended_lock[i + n][j + n] != 1:
                return False
    return True

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))