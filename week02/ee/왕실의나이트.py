# 실전 문제 2- 왕실의 나이트

position = input()
row = int(position[1]) - 1
col = int(ord(position[0]))-97

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
count = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row < 8 and next_row >= 0 and next_col < 8 and next_col >= 0:
        count += 1

print(count)

# 이미 답지 코드를 읽어버린 이상 이 방식으로 밖에 풀지 못 하겠따