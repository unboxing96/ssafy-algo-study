import sys
sys.stdin = open("05_32136_소신발언.txt")

def check(time): # 현재 time 내에 모든 얼음을 녹일 수 있는 히터의 위치가 있는지 ?
    left = -1e9
    right = 1e9

    for i in range(n):
        left = max(left, i - time // arr[i])
        right = min(right, i + time // arr[i]) # 히터를 설치할 수 있는 모든 인덱스를 나타내는 포인터

        if left > right:
            return False
    
    return True

n = int(input())
arr = list(map(int, input().split()))

low = 0
high = max(arr) * (n - 1) # time을 나타내는 포인터

while low < high:
    mid = (low + high) // 2
    if check(mid):
        high = mid
    else:
        low = mid + 1

print(low)