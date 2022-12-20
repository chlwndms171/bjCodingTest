l = []
for i in range(10):
    num = int(input()) % 42
    if num not in l:
        l.append(num)
print(len(l))