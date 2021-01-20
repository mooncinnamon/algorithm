import sys

loop_num = int(sys.stdin.readline().rstrip())
i = 0


def factorial(n):
    ret = 1
    for fac in range(1, n + 1):
        ret *= fac
    return ret


while i < loop_num:
    i += 1
    x, y = map(int, sys.stdin.readline().rstrip().split())

    num = int(factorial(y) // factorial(x) // factorial(y - x))
    print(num)
