
def binary_search(arr: list, target: int):
    left: int = 0;
    right: int = len(arr) - 1;

    while left < right:
        mid: int = (left + right) // 2;

        a: int = arr[mid];
        b: int = target;

        # 원하는 조건 구현 이상, 이하, 미만, 초과
        # 찾는 값이 현재 값보다 작은 경우 right 범위를 줄입니다.
        if a == b:
            return mid;
        if a > b:
            right = mid;

        # 찾는 값이 현재 값보다 큰 경우 left 범위를 줄입니다.
        elif a < b:
            left = mid + 1;

    return left;

arr: list[int] = [1, 2, 3, 4, 5, 6, 7];
idx: int = binary_search(arr, 7);

print(idx);
