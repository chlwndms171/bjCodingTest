import sys

stack = []

for i in range(int(sys.stdin.readline())):
    a=sys.stdin.readline().split()
    if a[0] == "pop":
        if len(stack)>0:
            print(stack.pop())
        else:
            print("-1")
    elif a[0] == "size":
        print(len(stack))
    elif a[0] == "empty":
        if len(stack)>0:
            print("0")
        else :
            print("1")
    elif a[0] == "top":
        if len(stack)>0:
            print(stack[-1])
        else:
            print("-1")
    else :
        stack.append(a[1])
        
# 반목문으로 입력받을 떄 input()으로 받으면 시간초과 뜨니까 sys.stdin.readline()으로 받을 것