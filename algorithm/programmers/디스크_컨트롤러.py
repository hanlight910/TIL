import heapq as hp;

def solution(jobs):
    answer = 0;
    sorted(jobs);
    length = len(jobs);

    idx = 0;
    current_time = 0;

    heap = [];
    # for i in range(0, length, 1):
    #     temp = jobs[i][0];
    #     jobs[i][0] = jobs[i][1];
    #     jobs[i][1] = temp;
    
    while idx < length or heap:
        while idx < length and jobs[idx][0] <= current_time:
            hp.heappush(heap, (jobs[idx][1], jobs[idx][0]));
            idx += 1;
        if heap:
            duration, start_time = hp.heappop(heap);
            answer += duration + current_time - start_time;
            current_time += duration;
        else:
            current_time = jobs[idx][0];
    return int(answer / length);

# print(solution( [[5, 10], [6, 8], [14, 2], [11, 5], [100, 7]]));
