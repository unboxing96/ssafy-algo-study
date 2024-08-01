N = int(input())
# 00시 00분 00초 ~ 00시 59분 59초까지 경우의수는 총 3600개
# 이를 000000 ~ 005959로 생각
sec = 60
minute = 60
count = 0
clock = ''
for i in range(N+1):
    for j in range(minute):
        for k in range(sec):
            clock += str(i) + str(j) + str(k)
            if '3' in clock:
                count += 1
                clock = ''



print(count)