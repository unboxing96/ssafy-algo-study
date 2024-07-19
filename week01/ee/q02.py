#곱하기 혹은 더하기

chars = input() #문자열 입력받기
result = 1
for char in chars:
    if char == '0' or char == '1': # 0이면 패스
        result += int(char)
    else: #숫자면 그냥 다 곱하기
        result *= int(char)
print(result)


