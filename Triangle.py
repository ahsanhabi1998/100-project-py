# # /////////////////Area of a Triangle////////////////////////.... বিষমবাহু ত্রিভুজ=.যে ত্রিভুজের বাহুগুলো পরস্পর অসমান তাকে বিষমবাহু ত্রিভুজ বলে
# import math
# def triangle_area_heron(a, b, c):
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     return area

# # Inputting the values of the three sides of the triangle
# a = float(input("Enter the first side length of the triangle: "))
# b = float(input("Enter the second side length of the triangle: "))
# c = float(input("Enter the third side length of the triangle: "))

# # Printing the result
# print("The area of the triangle is", triangle_area_heron(a, b, c))



# # /////////////////Area of a Triangle//////////////////////// ....সমকোণী ত্রিভুজ

# def triangle_area(base, height):
#     return 0.5 * base * height
# # Inputting the values of base and height
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))

# # Printing the result
# print("The area of the triangle is", triangle_area(base, height))

# # /////////////////Area of a Triangle//////////////////////// ....সমকোণী ত্রিভুজ **
# lombo= float (input("your inter lombo:"))
# vhumi = float (input('enter vhumi :'))
# khatrofol = (0.5)*lombo * vhumi
# print ("your khatrofol ",khatrofol)