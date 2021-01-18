import sys

loop_num = int(sys.stdin.readline().rstrip())
i = 0
while i < loop_num:
    i += 1
    x, y = map(int, sys.stdin.readline().rstrip().split())
    s = 1
    for z in range(0, y):
        s = s * x % 10
    if s == 0:
        print('10')
    else:
        print(s)
