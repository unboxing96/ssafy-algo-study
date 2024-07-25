import sys

sys.stdin = open('input.txt')

# 문자열 재정렬

# 1만개가 들어오는 문자열을 정렬하세요.
# 단, 숫자는 더해서 제일 뒤에 적기.

# INPUT 받은 값을 SORT한 후 isdigit()을 통해 NUMBER에 숫자 SUM. COUNT+1
# COUNT된 수량만큼 슬라이싱하고 요소 붙여넣고 출력.


A = input()
# SORT 진행
input_list = sorted(A)

number = 0
count = 0

# ISDIGIT()을 통해서 TRUE, FALSE체크.
for x in input_list:
    if x.isdigit() :
        number += int(x)
        count += 1
        
# 리스트 슬라이싱 및 더한 NUMBER 요소 추가해서 RESULT 반환
slice_list = input_list[count:]
slice_list.append(number)
result = ''.join(map(str,slice_list))
print(result)


# 공부한 내용
# isdigit()은 문자열 메서드로, 문자열이 숫자로만 구성되어있으면 TRUE 반환