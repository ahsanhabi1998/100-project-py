num1 = int ( input("enter fast number here: " ))
num2 = int ( input ( " enter second number here :" ))


while True:       
        choice  = int ( input( "enter your choice 1-4:"  ))
        if choice == 1 :
            print ("the addition of given tow number",num1+num2)
        elif choice== 2:
            print ("the subtraction  of given tow number", num1-num2)
        elif choice == 3:
            print ("the multiplication of given tow number",num1*num2)
        elif choice == 4:
            print ("the divition of given tow number",num1/num2)
        else :
            print("invalide input")
            break