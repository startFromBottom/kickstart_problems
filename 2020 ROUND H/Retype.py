def solution():
    # case 1 : 처음 부터 다시 시작
    case1 = K + N
    # case 2 : 검 있는데로 내려가고 나머지 올라감
    case2 = K + (K - S) + (N - S)
    print(case1, case2)
    return min(case1, case2)


if __name__ == "__main__":

    T = int(input())
    for i in range(T):
        N, K, S = map(int, input().split())

        print("Case #{}: {}".format(i + 1, solution()))
