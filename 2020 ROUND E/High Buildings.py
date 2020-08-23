T = int(input())


def find_high_buildings(N, A, B, C):
    if N == 1:
        if A == 1 and B == 1 and C == 1:
            return "1"
        return "IMPOSSIBLE"

    buildings = [0] * N
    if A < C or B < C:
        return "IMPOSSIBLE"

    if C >= 2:
        lo = A - C
        hi = N - 1 - (B - C)
        if hi - lo + 1 < C:
            return "IMPOSSIBLE"
        # Put all the buildings of height N between lo and hi.
        # In other cases(less than lo, more than hi), all heights are set to N-1.
        buildings[lo] = N
        buildings[hi] = N
        C -= 2
        for i in range(lo):
            buildings[i] = N - 1
        for j in range(hi + 1, N):
            buildings[j] = N - 1
        for k in range(lo + 1, hi):
            if C > 0:
                buildings[k] = N
                C -= 1
            else:
                buildings[k] = N - 1
    else:  # C = 1
        if (A + B > N + 1) or (A < 2 and B < 2):
            return "IMPOSSIBLE"
        l = A - C
        r = B - C

        # If l is larger, place the building of height N in (N-B-C-1).
        # To the right of the location, all buildings with a height of N-1 are placed,
        # and in the case of the left, N-1 buildings are placed as many as l,
        # and the rest are set to N-2.

        # Vice versa think the opposite
        if l >= r:
            buildings[N - 1 - r] = N
            for i in range(N - r - 1):
                if l > 0:
                    buildings[i] = N - 1
                    l -= 1
                else:
                    buildings[i] = N - 2
            for j in range(N - r, N):
                buildings[j] = N - 1
        else:
            buildings[l] = N
            for i in range(l):
                buildings[i] = N - 1
            for j in range(N - 1, l, -1):
                if r > 0:
                    buildings[j] = N - 1
                    r -= 1
                else:
                    buildings[j] = N - 2
    return " ".join(map(str, buildings))


for t in range(T):
    N, A, B, C = map(int, input().split())
    buildings = find_high_buildings(N, A, B, C)
    print("Case #{}: {}".format(t + 1, buildings))
