# >> 이진탐색을 효율적으로 해주는게 bisect 함수,
# 특정index가 들어갈 위치를 왼쪽이랑 오른쪽에서 계산해줘서 두개를 빼면 그 값을 가진 값들의 개수가 나옴
from bisect import bisect_left, bisect_right
import copy

def counts(arr, query):
    a = bisect_left(arr, query.replace("?", "a"))   # 문자데이터니까 a부터 z까지로 보고 개수 찾아야함
    z = bisect_right(arr, query.replace("?", "z"))
    return z-a      # fro?? 라던지 ????o 라던지 하는 단어 개수가 몇개가 있는가

def solution(words, queries):
    words.sort()
    words_reverse = copy.deepcopy(words)
    words_reverse = [i[::-1] for i in words_reverse] # 뒤집기
    words_reverse.sort() # 뒤집은거 정렬, 이 정렬한 데이터 안에서 이진탐색을 하는것임

    new_words = {}
    new_words_reverses = {}

    result = []

    for q in queries:
        if q[0] == '?': # 처음에 ?로 시작하는 쿼리라면 뒤집은 단어 있는 곳에서 찾아야함
            if len(q) not in new_words_reverses:
                new_words_reverses[len(q)] = [i for i in words_reverse if len(i) == len(q)] # 단어길이에 해당하는 lst만들기
                # 5 : [frame, froxx ... ] 이런꼴
            result.append(counts(new_words_reverses[len(q)], q[::-1]))
        else:
            if len(q) not in new_words:
                new_words[len(q)] = [i for i in words if len(i) == len(q)]
            result.append(counts(new_words[len(q)], q))
    return result

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))