import sys

row, column = map(int, sys.stdin.readline().rstrip().split())
i = 0

columnCheck = [0 for x in range(column)]
rowCheck = [0 for y in range(row)]
while i < row:
    tmp = str(sys.stdin.readline().rstrip())
    for j in range(len(tmp)):
        if tmp[j] == 'X':
            columnCheck[j] = 1
            rowCheck[i] = 1
    i += 1

print(columnCheck.count(0) if columnCheck.count(0) > rowCheck.count(0) else rowCheck.count(0))
