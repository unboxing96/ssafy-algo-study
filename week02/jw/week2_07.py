number = input()
list_number = list(n)
len_list = len(list_number)
half = len(list_number)/2

count = 0
result_1 = 0 # 첫번째 요소부터 합계
result_2 = 0 # 끝 요소부터 합계
for i in range(len_list):
    result_1 += int(list_number[i])
    result_2 += int(list_number[-i-1])
    count += 1
    if count == half: # 절반까지 다 합치면 중지
        break

if result_1 == result_2:
    print('LUCKY')
else:
    print('READY') 




