import sys

sys.stdin = open('input.txt')

# 숫자 0부터 9로만 이루어진 문자열S 주어짐.

S = input()

# 각숫자 사이에 * or +를 넣어서 결과적으로 가장 큰수 작성.

# 단어 split 필요함. 해서 int 0이면 더하고 외에 다곱하기.

result = 1

for puls_or_multiply in range(len(S)):
    if int(S[puls_or_multiply]) == 0 :
        pass
    else: 
        result = result * int(S[puls_or_multiply])

print(result)