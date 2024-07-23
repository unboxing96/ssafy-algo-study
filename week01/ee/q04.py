# 만들 수 없는 금액

n = int(input()) # 동전의 갯수

coins = list(map(int, input().split()))
coins.sort()

target = 1 #만들 수 없는 최소 금액

for coin in coins: # 1부터 차례대로 특정한 금액을 만들 수 있는지 확인
    if target < coin: # 만들 수 없는 금액을 찾았을 때 반복 종료
        break
    target += coin # 만들 수 있다면 

print(target)

# 못 풀었음 
# 답지 봤음. . .