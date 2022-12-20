n = int(input())
a = list(map(int, input().split()))
f = int(input())
# 
cnt = 0
for i in range(0, n):
    if (a[i] == f):
        cnt += 1
print(cnt)
# 
# 5줄 한 줄로 압축 가능.. 
# print(a.count(f))