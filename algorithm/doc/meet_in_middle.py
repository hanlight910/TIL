
def brute_force(sample: list) -> list[list]:
    full_set: list[list] = [];
    n: int =  len(sample);

    # 총 2^n 걸리므로 비트 연산자를 통해 2^n를 구합니다.
    for i in range(0, 1 << n):
        subset: list = [];

        for j in range(0, n):
            if i & (1 << j):
                subset.append(sample[j]);

        full_set.append(subset);

    return full_set;

sample: list[int] = [i for i in range(1, 3 + 1)];
power_set = brute_force(sample);
print(power_set);
