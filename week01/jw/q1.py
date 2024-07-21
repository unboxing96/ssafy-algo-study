n = int(input()) # 총 모험가 수
f_p = list(map(int, input().split())) # 공포도
f_p.sort() # 공포도 데이터 분리, 오름차순

result = 0 # 만드는 그룹 수
ad_num = 0 # 현재 그룹 내 모험가 수

for fear in f_p: # 공포도가 x인 사람은 그룹 내 최소한 x명이상이므로
    ad_num += 1
    if ad_num >= fear:
        result += 1
        ad_num = 0

print(result)
    

