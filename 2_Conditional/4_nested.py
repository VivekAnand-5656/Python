# --- Nested if else -------
angle1 = int(input("Enter First Angle :"))
angle2 = int(input("Enter Second Angle :"))
angle3 = int(input("Enter Third Angle :"))

if(angle1 == angle2):
    if(angle1 == angle3):
        print("Equilateral Triangle !")
    else:
        print("Not Triangle !")
else:
    if(angle2 == angle1 or angle2 == angle3 or angle1 == angle3):
        print("Isosceles Triangle !")
    else:
        if(angle1 != angle2 and angle1 != angle3 and angle2 != angle3):
            print("Scalene Triangle !")