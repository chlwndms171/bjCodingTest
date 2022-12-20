l=[i for i in range(1,31)]

for i in range(28):
    l.remove(int(input()))
    
print(min(l))
print(max(l))

# l = []
# for i in range(0,28):
#     l.append(int(input()))
# l.sort()
# n = 1
# if(l[0]!=1):
#     print(n)
#     n+=1
#     for i in range(0,28):
#         while(l[i]!=n):
#             print(n)
#             n+=1
#         n+=1
# else:
#     for i in range(0,28):
#         while(l[i]!=n):
#             print(n)
#             n+=1
#         n+=1
# if(n==29):
#     print(n)
#     print(n+1)
# elif(n==30):
#     print(n)
    