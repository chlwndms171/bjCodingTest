import sys

input = sys.stdin.readline()
n = int(input)
for i in range(0, n):
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(a+b)