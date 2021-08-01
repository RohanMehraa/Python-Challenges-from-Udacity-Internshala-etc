def close_ten(num):
    return ( abs(100-num) <= 10  or  abs(200-num) <= 10 )
choice = "Y"

while(choice == "y" or choice == "Y"):
    num = int(input("\nENTER ANY NO. :  "))
    print(close_ten(num))
    choice = str(input("\nDo you want to check another no. (Y/N)?    :    "))
