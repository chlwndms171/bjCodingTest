h, m = map(int, input().split())
t = int(input())
extra_h = (m+t)//60
extra_m = (m+t)%60
if(extra_h>=1):
    m = extra_m
    if(h+extra_h>23):
        h = h+extra_h-24
    else:
        h+=extra_h
else:
    m += t
print(h, m)