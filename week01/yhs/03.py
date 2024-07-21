S = list(map(int, input()))

print(S)

zeros = 0
ones = 0
last_num = S[0]


if last_num == 0:
    zeros +=1
else:
    ones += 1

for number in S:
    if number < last_num:
        last_num = number
        zeros += 1
    elif number > last_num:
        last_num = number
        ones += 1
    

print(zeros, ones)

if zeros > ones:
    print(ones)
else:
    print(zeros)
