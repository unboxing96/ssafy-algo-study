import sys
sys.stdin = open("숫자카드게임.txt", "r")

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

maxNum = -10001
for elem in matrix:
    maxNum = max(maxNum, min(elem))

print(maxNum)