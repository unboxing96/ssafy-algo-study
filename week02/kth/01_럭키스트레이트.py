import sys
sys.stdin = open("01_럭키스트레이트.txt", "r")

score = [int(elem) for elem in input()]
print("LUCKY" if sum(score[:len(score) // 2]) == sum(score[len(score) // 2:]) else "READY")