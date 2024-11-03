# 이동 10초 전
# 이동 10초 후
# opstart <= 현재 재생 위치 <= op_end -> op_end

def time_convert_to_second(time: str) -> int:
    minutes: int = int(time[0:2]) * 60;
    second: int = int(time[3:5]);
    return second + minutes;

def convert_second_to_time(time: int) -> str:
    minutes: int = int(time / 60);
    seconds: int = time - (minutes * 60);
    str_minutes = chr(int(minutes / 10) + 48) + chr(int(minutes % 10) + 48);
    str_seconds = chr(int(seconds / 10) + 48) + chr(int(seconds % 10) + 48);
    return str_minutes + ":" + str_seconds;

def operation(time: int, command: str, max_len: int):
    if command == "next":
        time = time + 10 if time + 10 < max_len else max_len;
    elif command == "prev":
        time = time - 10 if time - 10 > 0 else 0;
    return time;
        
def solution(video_len, pos, op_start, op_end, commands):
    pos_seconds: int = time_convert_to_second(pos);
    op_start_seconds: int = time_convert_to_second(op_start);
    op_end_seconds: int = time_convert_to_second(op_end);
    video_len_seconds: int = time_convert_to_second(video_len);
    
    for command in commands:
        if op_start_seconds <= pos_seconds and (pos_seconds <= op_end_seconds):
            pos_seconds = op_end_seconds;

        pos_seconds = operation(pos_seconds, command, video_len_seconds);

    if op_start_seconds <= pos_seconds and (pos_seconds <= op_end_seconds):
        pos_seconds = op_end_seconds;

    answer = convert_second_to_time(pos_seconds);
    return answer

