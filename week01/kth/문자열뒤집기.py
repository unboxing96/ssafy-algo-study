import sys
sys.stdin = open("문자열뒤집기.txt", "r")

# 문제 분석
# 연속한 문자열을 뒤집을 수 있다. (뒤집다: 0 -> 1 or 1 -> 0)
# 뒤집기 최소 횟수를 출력하라

# 접근
# 연속된 0 혹은 1을 기준으로 덩어리를 분리한다.
# 더 적은 쪽의 개수를 return 한다.
# 분리할 것도 없다. 개별 카운트 변수를 두고 세자.

string = input()

countZero = 0
countOne = 0

if string[0] == "0":
    countZero += 1
else:
    countOne += 1

for idx in range(1, len(string)):
    if string[idx - 1] == string[idx]:
        pass
    else:
        if string[idx] == "0":
            countZero += 1
        else:
            countOne += 1

print(min(countZero, countOne))