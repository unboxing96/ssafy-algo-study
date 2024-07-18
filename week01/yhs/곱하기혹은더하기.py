numbers = list(map(int, input()))

ans = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < 2 or ans < 2:
        ans += numbers[i]
    else:
        ans *= numbers[i]

print(ans)
