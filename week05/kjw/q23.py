import sys
sys.stdin = open('input.txt')
n = int(input())
data = [tuple(map(str, input().split())) for _ in range(n)]
m = len(data)
'''
1. 국어점수 감소순
2. 영어점수 증가순
3. 수학점수 감소순
4. 이름증가순, 대문자가먼저, 그다음소문자
대문자A는 65 소문자a는 97 문자0은 48 486597 알고있기, 쓰는함수는 ord(영어) chr(숫자)로 확인가능
'''

data.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])) # 국어점수 감소순

for i in range(m):
    print(data[i][0])