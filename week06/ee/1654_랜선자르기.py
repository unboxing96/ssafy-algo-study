import sys
sys.stdin = open("1654_input.txt")

K, N = map(int, sys.stdin.readline().split()) #영식이의 랜선 개수 K, 필요한 랜선 개수 N
lans = [int(sys.stdin.readline()) for _ in range(K)] #랜선 길이

# print(lans)

#제각각인 랜선의 길이를 모두 N개의 같은 길이의 랜선으로 만들기
#만들 수 있는 최대 랜선의 길이

#뭘 찾을 것인가?
#자를 랜선의 길이?

lans.sort() #정렬부터 하공

def cut_lan(length):
    result = 0
    for lan in lans:
        result += lan//length

    return result

left = 1
right = lans[-1]

while left <= right:
    mid = (left + right)//2

    temp = cut_lan(mid)
    if temp >= N:
        left = mid + 1
    elif temp < N:
        right = mid - 1

print(right)
