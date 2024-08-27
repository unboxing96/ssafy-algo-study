# 문제 분석
# 와일드카드 문자는 개수까지 동일해야 한다.
# queries 배열의 각 쿼리가 words의 몇 개의 단어와 일치하는지 카운트 해서 배열로 반환
# words에 중복은 없다.
# queries 중복될 수 있다.
    # ?는 반드시 하나 이상 있다.
    # ?는 접두사 혹은 접미사 중 하나로만 주어진다. 양쪽에 있을 수 없다.

def binary_search(words, query):
    start, end = 0, len(words)
    while start < end:
        mid = (start + end) // 2
        if words[mid] < query:
            start = mid + 1
        else:
            end = mid
    # 왼쪽 경계값을 찾는 경우, end는 query가 처음으로 나타나는 위치
    # 오른쪽 경계값을 찾는 경우, end는 query가 초과되는 위치를 가리킵니다.
    return end

def solution(words, queries):
    answer = []
    word_cnt_arr = [[] for _ in range(10001)]
    reverse_word_cnt_arr = [[] for _ in range(10001)]

    for word in words:
        word_cnt_arr[len(word)].append(word)
        reverse_word_cnt_arr[len(word)].append(word[::-1])
        
    for i in range(10001):
        word_cnt_arr[i].sort()
        reverse_word_cnt_arr[i].sort()
    
    for query in queries:
        query_to_A = query.replace('?', 'a')
        query_to_Z = query.replace('?', 'z')
        
        if query[0] == '?':
            start = binary_search(reverse_word_cnt_arr[len(query)], query_to_A[::-1])
            end = binary_search(reverse_word_cnt_arr[len(query)], query_to_Z[::-1])
            answer.append(end - start)
        else:
            start = binary_search(word_cnt_arr[len(query)], query_to_A)
            end = binary_search(word_cnt_arr[len(query)], query_to_Z)
            answer.append(end - start)
    

    
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = solution(words, queries)
print(result)