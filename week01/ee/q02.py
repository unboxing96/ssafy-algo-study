#곱하기 혹은 더하기

chars = input() #문자열 입력받기
result = 1
if chars == '0':
    result = 0
else:
    for char in chars:
        if char == '0' or char == '1': # 1이면 더하기
            result += int(char)
        else: #이외에는 그냥 다 곱하기
            result *= int(char)
print(result)



