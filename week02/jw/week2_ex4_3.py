N = list(map(str, input()))
x = ord(N[0]) -96 # a부터h를 97부터 104로 생각
y = int(N[1])

dx = [-2, 2, -2, 2, -1, 1, -1, 1]
dy = [-1, -1, 1, 1, -2, -2, 2, 2]
move_type = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


# 처음엔 예시1번처럼 풀려고 했는데 하고보니까 move_type은 설정 필요없고 그냥 숫자8로 했어도 됐음
count = 0
for i in range(len(move_type)):
    x += dx[i]
    y += dy[i]
    if x < 1 or y < 1:
        pass
    elif x > 8 or y > 8:
        pass
    else:
        count += 1
        x = ord(N[0]) - 96
        y = int(N[1])

print(count)
# y축 증가가 y값이 증가라는 고정관념 버리기 이거땜에 20분 낭비..