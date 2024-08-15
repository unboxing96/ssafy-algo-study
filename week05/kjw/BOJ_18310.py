''' 시간초과 ㅋㅋ
n = int(input())
data = list(map(int, input().split()))

lst = []
for i in data:
    total = 0
    for j in data:
        total += abs(i-j)
    lst.append((total,i))


lst.sort(key=lambda x: x[0])
print(lst[0][1])
'''

# 아 이거 미분이구나;;
n = int(input())
data = list(map(int, input().split()))

data.sort()
length = len(data)
print(data[(length-1)//2])