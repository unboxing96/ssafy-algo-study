# 문자열 뒤집기
s = input()
number = list(s)

first_result = 0
for i in range(len(number)-1):
    if number[i] != number[i+1]:
        first_result += 1 


if first_result % 2 == 0: # 1과 0이 짝수번 바뀌면 ex)10101
    final_result = first_result // 2
else:                       # 1과 0이 홀수번 바뀌면 
    final_result = (first_result+1) // 2

print(final_result)


