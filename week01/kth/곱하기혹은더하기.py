import sys
sys.stdin = open("곱하기혹은더하기.txt", "r")

# 문제 분석
# 숫자로된 문자열이 입력된다
# 곱하기 혹은 더하기 연산으로 최댓값을 return 하라
# 사칙연산의 우선순위 규칙을 무시하고, 문자열의 첫 번째 인자부터 차례대로 계산된다.

# 접근
# 0과 1을 제외하면 곱하기가 무조건 더 좋다.
# 문자열을 반복하며, 현재 원소가 0 혹은 1이라면, 더한다. 나머지는 곱한다.
    # tot 혹은 현재 원소가 0 혹은 1이라면 더한다.
    # 나머지는 곱한다.

string_num = input()

tot = 0
for elem in string_num:
    elem = int(elem)

    if tot == 0 or tot == 1 or elem == 0 or elem == 1:
        tot += elem
    else:
        tot *= elem

print(tot)