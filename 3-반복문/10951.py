import sys

input = sys.stdin.readline()
a, b = map(int, input.split())
while (True):
    try:
        print(a+b)
        input = sys.stdin.readline()
        a, b = map(int, input.split())
    except:
        break