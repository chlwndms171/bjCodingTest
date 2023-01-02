n, price = map(int, input().split())
p_list = []
min = 0

for i in range(n):
    p_list.append(int(input()))
    
p_list.reverse() 
while price > 0 :
    for i in range(n):
        while price >= p_list[i]:
            min += price // p_list[i]
            price -= price // p_list[i] * p_list[i] # price = price % p_list[i] 나머지를 바로 저장해주면 될듯
    break

print(min)
           
# 시간초과
# n, price = map(int, input().split())
# p_list = []
# min = 0

# for i in range(n): # 원소의 개수가 n개일 때 
#     p_list.append(int(input()))

# while price > 0 :
#     for i in reversed(range(n)):
#         while price >= p_list[i]:
#             price -= p_list[i]
#             min += 1
#     break
            
# print(min)