n, x = map(int, input().split())
l = list(map(int, input().split()))
r = []
for i in range(0,n):
    if(l[i]<x):
        r.append(l[i])
print(*r)
# for i in range(n):
#     if l[i] < x:
#         print(l[i], end=" ")