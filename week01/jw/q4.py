n = int(input())
coin = list(map(int, input().split()))
coin.sort()

# 수직선 위에서 i칸만큼 점프뛴다고 생각
  
result = 1 
for i in coin:
    if i > result: # 내가 서있는 위치보다 큰 값만큼 뛸 수는 없음
        break
    else: # 뛸 수 있는 거리 향상
        result = result + i

print(result)