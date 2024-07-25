# 문자열 재정렬

# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에
# 모든 숫자를 더한 값을 이어서 출력

S = input()
num_sum = 0
chars = []

for char in S:
    if char.isdecimal(): # 숫자면 더해서 num_sum에 저장
        num_sum += int(char)
    else:               # 문자면 배열에 넣기
        chars.append(char)

chars = ''.join(sorted(chars)) # 배열 정렬하고 문자열로 변환
 
print(chars+str(num_sum))