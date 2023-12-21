num1 = int (input("enter 1st number:"))
num2 = int (input("enter 2nd number:"))
num3 = int (input("enter 3rd number:"))

if (num1 > num3 ) and (num1>num2):
    print ("is the largest number =",num1)
elif (num2 > num1) and (num2> num3):
    print ("is the largest number=",num2)
else:
    print ("is the lergest number=",num3)