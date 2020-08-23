def longest_arithmetic(arr: list) -> int:
    l = len(arr)

    if l == 2:
        return l

    last_dif = arr[1] - arr[0]
    max_longest = 2
    longest = 2

    for i in range(2, l):
        dif = arr[i] - arr[i - 1]
        if dif == last_dif:
            longest += 1
        else:
            max_longest = max(max_longest, longest)
            longest = 2
            last_dif = dif
    # last chec k
    max_longest = max(max_longest, longest)

    return max_longest


T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split(" ")))
    res = longest_arithmetic(arr)

    print("Case #{}: {}".format(t + 1, res))
