import heapq as hp;

def solution(scoville, K):
    answer = 0;
    heap = scoville;
    hp.heapify(heap);
    
    while len(heap) > 0 and heap[0] < K:
        min = hp.heappop(heap);
        second_min = hp.heappop(heap);
        new = min + (second_min * 2);
        hp.heappush(heap, new);
        answer += 1;

    if len(heap) == 0:
        answer = 0; 

    return answer;

# print(solution([1, 2, 3, 9, 10, 12], 7));
