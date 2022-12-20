n = int(input())
for i in range(n):
    s=input()
    l=list(s)
    sum = 0
    cnt = 0
    for j in range(len(l)):
        if(l[j]=="O"):
            cnt+=1
            sum += cnt
        else:
            cnt = 0
    print(sum)
            
