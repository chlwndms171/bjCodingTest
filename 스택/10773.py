import sys

num = []

for i in range (int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0 :
        num.pop()
    else:
        num.append(n)

print(sum(num))