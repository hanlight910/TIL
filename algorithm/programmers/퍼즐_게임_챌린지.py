def is_valid(diffs: list, times: list, limit: int, level: int):
    length: int = len(diffs);
    sum: int = 0;

    prev_cost: int = 0;

    for i in range(0, length):
        if level >= diffs[i]:
            sum += times[i];
            
        else:
            sum += ((diffs[i] - level) * (times[i] + prev_cost));
            sum += times[i];
        prev_cost = times[i]
        if limit < sum:
            return 0;

    return 1;

def solution(diffs, times, limit):
    answer = 0;
    left: int = 0;
    right: int = max(diffs);
    while left < right:
        mid: int = int((right + left) / 2);
        if is_valid(diffs, times, limit, mid):
            right = mid;
        else:
            left = mid + 1;
    
    answer = left;
    return answer;

ans = solution([1, 1, 3], [1, 1, 3], 50);
print(ans);

