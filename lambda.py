# x= lambda a : a + a 
# print(x(10))

# # sum = lambda a,b : a + b
# # print(sum(20,30))

# # sum= lambda a ,b,c: a+b+c
# # print(sum(10,20,30))

# def add (n):
#     return lambda a :a+n 
# sum = add(10)
# print(sum(20))

# l=[20,30,50,44,77,60,100,96,64 ,39,26]
# result =list (filter(lambda b: b % 13 == 0,l ))
# print(result)

ugers = int (input("enter ugears input: "))
ltrt_1 = 100
total_sum = lambda ugers : ugers *ltrt_1
s1=(ugers)
print( total_sum (s1))