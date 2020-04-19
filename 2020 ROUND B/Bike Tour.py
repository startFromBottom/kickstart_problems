"""

link : https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6

"""

T = int(input())

for t in range(T):
    H = int(input())
    c = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(c) - 1):
        if c[i] > c[i-1] and c[i] > c[i+1]:
            ans += 1
    print("Case #{}: {}".format(t+1, ans))