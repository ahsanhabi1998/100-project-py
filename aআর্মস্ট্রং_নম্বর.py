# num = int (input("enter your number:"))
# sum = 0
# temp = num

# while temp > 0:
#     digit = temp % 10
#     cube = digit**3
#     sum = sum +cube
#     temp //=10
#     if sum == sum :
#         print("it is an Armstrong Number")
#     else:
#         print("it is  not an Armstrong Number")
    
    
lower = int (input ("lower number"))
upper = int (input ("upper number:"))
    
for num in range (lower,upper +1):
        order = len (str(num))
        sum =  0
        temp = num
        while temp >0:
            digit = temp%10
            sum += digit**order
            temp//=10
            if sum == sum :
                print(sum)
            