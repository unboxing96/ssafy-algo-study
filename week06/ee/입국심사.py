def solution(n, times):
    times.sort()

    left = times[0]
    right = times[-1] * n

    def test(mid): #심사
        ans = 0
        for time in times:
            ans += mid // time
        return ans

    while left < right:
        mid = (left + right) // 2
        temp = test(mid)

        if temp >= n: #더 많은 사람을 심사할 수 있다면
            right = mid #시간을 좀 더 줄여도 됨
        else: #n명을 심사할 수 없다면
            left = mid + 1#시간을 좀 더 늘려야됨

    return left # 마지막에는 mid값이 갱신되지 않기 때문에 left나 right값을 반환

print(solution(6, [7,10])) #28