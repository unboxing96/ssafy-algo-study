import sys

sys.stdin = open('input.txt')


# 문제 이해: 정수 n이 입력되었는데 3이 하나라도 포함되는 경우의 수를 구하시오.
# 시간만 주어지며, 3이 하나라도 있으면 count 1을 추가.

# 출력할 경우의 수 


def is_three(hour): 
    count = 0
    for h in range(hour+1):
        for m in range(60) :
            for s in range(60):
                #  만약 s에 3이있니? 있으면 +1 포멧팅 2자리로 만들기
                if '3' in f'{h:02}{m:02}{s:02}':
                    count += 1

    return count

hour = int(input())

print(is_three(hour))
