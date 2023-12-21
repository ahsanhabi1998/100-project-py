# ফিবোনাচি ক্রম
a =0
b =1
number = int (input ("enter your nurmber:"))
if number ==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,number):
        c = a + b
        a = b
        b = c
        print (c)
        
        