c = int(input())
for i in range (c):
    score = list(map(int, input().split()))
    n = score[0]
    score = score[1:]
    avg = sum(score)/n
    cnt = 0
    for j in range(n):
        if (score[j]>avg):
           cnt+=1
    result = cnt/n*100
    print("{:.3f}%".format(result)) 