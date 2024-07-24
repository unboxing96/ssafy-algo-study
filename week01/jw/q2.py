n = input()
numlist = [int(digit) for digit in n]

result = 0

for element in numlist:
    if result == 0 or result == 1 or element == 0 or element == 1:
        # n번째 수까지 합이 0이나 1, 자릿수가 0이나 1인 경우에는 덧셈  
        result += element
    else:
        # 그 외의 경우에는 곱셈
        result *= element


print(result)

