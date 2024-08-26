def solution(words, queries):
    answer = []

    words.sort(key=lambda x: (len(x), x))
    reverse_words = sorted(words, key=lambda x: (len(x), x[::-1]))

    for query in queries:

        token_idx = []
        for i in range(len(query)):  # ? 가 아닌 글자의 인덱스 저장
            if query[i].isalpha():
                token_idx.append(i)

        if not token_idx:  # query가 모두 '?' 인 경우: 길이만 같으면 ok
            ans = 0
            for word in words:
                if len(query) == len(word):
                    ans += 1
            answer.append(ans)
            continue

        if token_idx[0]:  # ???abc 와 같은 형태일 경우: 단어의 역순대로 정렬한 리스트에서 탐색
            s = find_start(query, token_idx, reverse_words)
            if s < 0:  # 찾지 못했다면 0
                answer.append(0)

            else:
                e = find_end(query, token_idx, reverse_words, s)
                answer.append(e - s + 1)

        else:  # abc???와 같은 형태일 경우: 단어를 올바른 순서대로 정렬한 리스트에서 탐색
            s = find_start(query, token_idx, words)
            if s < 0:  # 찾지 못했다면 0
                answer.append(0)

            else:
                e = find_end(query, token_idx, words, s)
                answer.append(e - s + 1)

    return answer


def find_start(query, idx, words):
    s1, e1 = 0, len(words) - 1  # 시작 위치 찾기
    ans = -1

    while s1 <= e1:
        m1 = (s1 + e1) // 2

        word = words[m1]

        if len(query) > len(word):  # 찾는 단어의 길이가 더 짧을 때 : 오른쪽에서 탐색
            s1 = m1 + 1

        elif len(query) < len(word):  # 찾는 단어의 길이가 더 길 때 : 왼쪽에서 탐색
            e1 = m1 - 1

        else:
            for i in idx:
                token, letter = query[i], word[i]
                if token > letter:  # 더 이전 순서의 알파벳일 때 : 오른쪽에서 탐색
                    s1 = m1 + 1
                    break
                elif token < letter:  # 더 나중 순서의 알파벳일 때 : 왼쪽에서 탐색
                    e1 = m1 - 1
                    break
            else:
                ans = m1
                if m1:
                    prev_word = words[m1 - 1]
                    if not find(query, idx, prev_word):  # 이전 단어가 키워드 포함 X
                        return m1
                    else:
                        e1 = m1 - 1
                else:
                    return m1

    return ans


def find_end(query, idx, words, m1):
    s2, e2 = m1, len(words) - 1  # 시작 위치 찾기
    ans = -1

    while s2 <= e2:
        m2 = (s2 + e2) // 2
        word = words[m2]

        if len(query) > len(word):  # 찾는 단어의 길이가 더 짧을 때 : 오른쪽에서 탐색
            s2 = m2 + 1

        elif len(query) < len(word):  # 찾는 단어의 길이가 더 길 때 : 왼쪽에서 탐색
            e2 = m2 - 1

        else:
            for i in idx:
                token, letter = query[i], word[i]

                if token > letter:  # 더 이전 순서의 알파벳일 때 : 오른쪽에서 탐색
                    s2 = m2 + 1
                    break
                elif token < letter:  # 더 나중 순서의 알파벳일 때 : 왼쪽에서 탐색
                    e2 = m2 - 1
                    break
            else:
                ans = m2
                if m2 >= len(words) - 1:
                    return m2
                next_word = words[m2 + 1]
                if not find(query, idx, next_word):  # 다음 단어가 키워드 포함 X
                    return m2
                else:
                    s2 = m2 + 1

    return ans


# 웨?  ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ ㅜ

def find(query, idx, word):
    if len(query) != len(word):             # query와 word의 길이가 다른 경우: 0 반환
        return 0

    for i in idx:
        token, letter = query[i], word[i]

        if token != letter:                 # query와 word가 일치하지 않는 경우: 0 반환
            return 0

    # 위의 조건에 걸리지 않는 경우: 1 반환(query와 word가 일치)
    return 1
