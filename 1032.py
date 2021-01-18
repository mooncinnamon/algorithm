import sys

loopNum = int(sys.stdin.readline().rstrip())
i = 0

texts = []

while i < loopNum:
    i += 1
    text = sys.stdin.readline().rstrip()
    texts.append(text)

pattern = []
for txt in texts:
    if not pattern:
        pattern = list(txt)
    else:
        for n in range(0, len(txt)):
            if pattern[n] != txt[n]:
                pattern[n] = '?'

print(''.join(pattern))
