import sys
sys.stdin = open("07_럭키스트레이트.txt", "r")

score = list(map(int, input()))
print("LUCKY" if sum(score[:len(score) // 2]) == sum(score[len(score) // 2:]) else "READY")