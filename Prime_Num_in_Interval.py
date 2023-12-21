lower = int (input("enter lower number:"))
uppur = int (input("enter upper number:"))
for num in range (lower,uppur +1):
    if num > 1:
        for i in range (2,num):
            if num % i == 0:
                break
        else:
            print(num)
                
    
        