# (r, c) 좌표

class Point:
    def __init__(self, x: int, y: int):
        self.x = x;
        self.y = y;

def solution(points, routes):
    answer = 0;

    visited: list[list[list[int]]] = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(10001)];

    for route in routes:
        times = 0;
        start = route[0];
        last_point = len(route) - 1;
        # print("---");
        for i in range(1, last_point + 1):
            end = route[i];

            start_y = points[start - 1][0];
            start_x = points[start - 1][1];
            end_y = points[end - 1][0];
            end_x = points[end - 1][1];
            
            while start != end:

                if visited[times][start_y][start_x] == 0:
                    visited[times][start_y][start_x] = 1;
                elif visited[times][start_y][start_x] == 1:
                    # print("trapped")
                    # print(f"times: {times}; {start_y}, {start_x}");
                    # print("trapped")
                    answer += 1;
                    visited[times][start_y][start_x] += 1;
                # print(f"s_y: {start_y}; s_x: {start_x}; e_y: {end_y}; e_x: {end_x}");
                if start_y > end_y:
                    start_y -= 1;
                elif start_y < end_y:
                    start_y += 1;
                elif start_x > end_x:
                    start_x -= 1;
                elif start_x < end_x:
                    start_x += 1;
                # print(f"times: {times}; {start_y}, {start_x}");


                if (start_y == end_y) and (start_x == end_x):
                    start = end;
                times += 1;

        last_point_y = points[route[last_point] - 1][0];
        last_point_x = points[route[last_point] - 1][1];

        if visited[times][last_point_y][last_point_x] == 0:
            visited[times][last_point_y][last_point_x] = 1;
        elif visited[times][last_point_y][last_point_x] == 1:
            # print("trapped")
            # print(f"times: {times}; {last_point_y}, {last_point_x}");
            # print("trapped")
            answer += 1;
            visited[times][last_point_y][last_point_x] += 1;

    return answer

point_1 = [[3, 2], [6, 4], [4, 7], [1, 4]];
routes_1 = [[4, 2], [1, 3], [2, 4]];

point_3 = [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]];
routes_3 = [[2, 3, 4, 5], [1, 3, 4, 5]];

point_4 =  [[1, 1], [2, 2], [3, 3]];
routes_4 = [[1, 2, 1], [3, 2, 1]];

point_100 =  [[1, 1], [1, 100], [100, 1], [100, 100]]
routes_100 = [[1, 2, 3, 4]];

print(solution(point_1, routes_1));
print(solution(point_3, routes_3));
print(solution(point_4, routes_4));
print(solution(point_100, routes_100));
