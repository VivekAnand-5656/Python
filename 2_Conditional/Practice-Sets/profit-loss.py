# .Write a C program to input cost price and selling price of a product and check profit or loss using if-else.
costPrice = int(input("Enter Cost Price:-"))
sellPrice = int(input("Enter Selling Price:-"))

if(costPrice < sellPrice):
    print("Profit!")
else:
    print("Loss!")