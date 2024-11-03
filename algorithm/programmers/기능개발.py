def get_rounded_quotient(dividend, divisor) -> int:
    return dividend / divisor if dividend % divisor == 0 else int(dividend / divisor) \
        + 1;

def solution(progresses, speeds):
    answer: list = [];
    stack = [];    
    stack.append(get_rounded_quotient((100 - progresses[0]), speeds[0]));
    cnt: int = 1;
    for i in range(1, len(progresses), 1):
        cur_day = get_rounded_quotient((100 - progresses[i]), speeds[i]);
        
        print(stack[0], cur_day);

        # 나중에 들어오는 일의 처리 수치가 이전보다 작거나 같으면
        # 배포 개수에 추가, 이제 필요 없으니 추가 로직 x
        if stack[0] >= cur_day:
            cnt += 1;
        else:
            stack.pop(0);
            answer.append(cnt);
            stack.append(cur_day);
            cnt = 1;

    if len(stack) > 0:
        answer.append(cnt);

    return answer;

# answer: list = solution([95, 95, 95, 95], [4, 3, 2, 1]);
# print(answer);

