"""

problem link : https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf

"""


def solution(D: int, r: list):
    """

    Time Complexity : O(n)

    각 버스 시간 주기 별로, r의 원소들을 역순으로 for문 돌려
    D(도착 시간)에 가장 근접하게끔 값을 곱해주어 temp 리스트에 추가

    ex)
    D = 1000
    r = [10, 20, 40, 900]
    -> temp = [ 900 * 1, 400 * 22, 20 * 44, 10 * 88] (temp[i]는 temp[i-1]보다 항상 작거나 같아야 한다.

    """
    if len(r) == 1:
        return r[0] * (D // r[0])
    max_val = r[-1] * (D // r[-1])
    temp = [max_val]
    for i in range(len(r) - 1, -1, -1):
        temp.append(r[i] * (temp[-1] // r[i]))
    return temp[-1]


T = int(input())

for t in range(T):
    N, D = tuple(map(int, input().split()))
    r = list(map(int, input().split()))
    print("Case #{}: {}".format(t + 1, solution(D, r)))
