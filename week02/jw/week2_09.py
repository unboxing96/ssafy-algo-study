def solution(s):
    s_length = len(s)


    # 길이가 n이면 2//n까지 자를 수 있는 경우의 수가 생김, 홀수여도 n//2 까지

    for i in range(1,s_length//2 + 1): # 1개자르기 ~ n//2개 자르기, (i개자르기)
        empty_list = []
        prev_str = s[0 : i]
        count = 1
        for j in range(i, s_length+1, i):
            cur_str = s[j : j+i]
            if prev_str == cur_str:
                count += 1
            elif prev_str!= cur_str:
                if count>=2:
                    empty_list.append(str(count))
                empty_list.append(prev_str)

            
                count = 1
        else:
            empty_list.append(s[j:])

    answer = 0
    return answer
# 아아아아아아ㅏ앙아아망런마ㅣㅇ러마ㅣㄴ어람피ㅏ