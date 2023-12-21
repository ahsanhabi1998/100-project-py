year = int (input("enter your  year:"))
if (year % 400 == 0) and ( year % 100 == 0):
    print("is a  Leap Year :",year)
elif( year % 4 == 0) and (year % 100 !=0):
    print ("is  a leap year :",year)
else :
    print("is not a leap year :",year)