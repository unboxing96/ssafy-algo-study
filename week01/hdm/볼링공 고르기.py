import sys

sys.stdin = open('index.txt')


N, M = map(int, input().split())
boll = list(map(int,input().split())) # [1, 3, 2, 3, 2]

count =0

for i in range(N) :

    
    for k in range(N) :
        if boll[i] != boll[k] : #1일때 3
            count +=1


count /= 2

print(int(count))