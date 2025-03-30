# Write a C program to check whether a triangle is valid or not if angles are given.

angle1 = int(input("Enter Angle 1:"))
angle2 = int(input("Enter Angle 2:"))
angle3 = int(input("Enter Angle 3:"))
check = angle1+angle2+angle3
if(check == 180 and (angle1 > 0 and angle2 > 0 and angle3 > 0)):
    print("Triangle is Valid!")
else:
    print("Not Triangle!")