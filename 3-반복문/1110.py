a=int(input())
b=a
cnt = 0
if(b<10):
    b=b*10+b
    cnt+=1
else:
    b=b%10*10+((b//10+b%10)%10)
    cnt+=1
while(a!=b):
    if(b<10):
        b=b*10+b
        cnt+=1
    else:
        b=b%10*10+((b//10+b%10)%10)
        cnt+=1
print(cnt)