N = int(input())
route = list(map(str, input().split()))

x, y = 1, 1

for i in route:
    if i == 'R' and y != N:
        y += 1
    elif i == 'L' and y != 1:
        y -= 1
    elif i == 'U' and x != 1:
        x -= 1
    elif i == 'D' and x != N:
        x += 1

print(x, y)