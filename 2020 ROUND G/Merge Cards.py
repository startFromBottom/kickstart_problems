from collections import deque


def factorial(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


def solution():
    total = 0
    q = deque()
    for i in range(1, N):
        temp = cards[:]
        temp[i - 1] += temp.pop(i)
        q.append((temp, temp[i - 1]))

    while q:
        sub, sc = q.popleft()
        l = len(sub)
        if l == 1:
            total += sc
        for i in range(1, l):
            temp = sub[:]
            temp[i - 1] += temp.pop(i)
            q.append((temp, sc + temp[i - 1]))

    return total / factorial(N - 1)


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        N = int(input())
        cards = list(map(int, input().split()))
        print("Case #{}: {}".format(i + 1, solution()))
