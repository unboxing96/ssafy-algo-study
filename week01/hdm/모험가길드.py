import sys

sys.stdin = open('input.txt')

N = int(input()) # 5
X = list(map(int, input().strip().split())) # 2 3 1 2 2
# 리스트 정렬해서 작은 그룹부터 묶기.
max_num = sorted(X) # 1 2 2 2 3
# 그룹 수 
group = 0
# 현재 그룹에 포함된 모험가 수
current_group =0

for fear in X :
    current_group += 1 # 1 / 2
    if current_group >= fear : # 1 / 2 
        group += 1
        current_group =0

print(group)
   




