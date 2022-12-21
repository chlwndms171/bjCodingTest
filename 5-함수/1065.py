n = int(input())
def d(n):
    sum = 0
    if(n<100):
        sum = n
    else:
        sum += 99
        for i in range(100, n+1):
            a = i//100
            c = i%10
            b = i//10%10
            if((b-a) == (c-b)):
                sum += 1
    print(sum)
d(n)
