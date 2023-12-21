# # multiplication= int(input("inter your number"))
# # for i in range (1,11):
# #     print(multiplication , "X", i,  "=", multiplication*i  )
    
# import time    
# num = int (input("enter your number:"))

# for i in range (1,11):
#     time.sleep(2)
#     print(num,"x", i , "=" , num%i)
n = int (input("enter your number :"))
index = 1
while index <= n:
    print( n,"x" ,index, "=", n*index)
    index +=1