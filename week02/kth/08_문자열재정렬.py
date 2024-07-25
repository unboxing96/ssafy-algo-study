import sys
sys.stdin = open("08_문자열재정렬.txt", "r")

word = input()
result = ""

num_tmp = 0
str_tmp = ""

for elem in word:
    if elem.isnumeric():
        num_tmp += int(elem)
    else:
        str_tmp += elem

result = "".join(sorted(str_tmp)) + str(num_tmp)
print(result)